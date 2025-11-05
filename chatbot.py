from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from openai import OpenAI
import datetime, os, time, csv

# --- Flask setup ---
app = Flask(__name__)
CORS(app)

# --- Model & session config ---
MODEL_NAME = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
SESSION_TIMEOUT_SECONDS = 15 * 60  # 15 minutes
all_sessions = {}  # {(response_id): {"messages": [...], "last_active": ts}}

# --- OpenAI client (key from Replit Secrets) ---
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("WARNING: OPENAI_API_KEY environment variable is not set. Chat functionality will not work.")
    print("Please add your OpenAI API key to Replit Secrets.")
    client = None
else:
    client = OpenAI(api_key=api_key)

def trim_history(messages, max_exchanges=10):
    """Keep only the last few message pairs to save tokens."""
    if not messages:
        return []
    system_msg = messages[0]
    convo = messages[1:]
    if len(convo) > 2 * max_exchanges:
        convo = convo[-2 * max_exchanges:]
    return [system_msg] + convo

@app.route("/")
def serve_ui():
    response = send_file("chat.html")
    # Disable caching to ensure updates are visible in iframes
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json or {}
    user_input = (data.get("message") or "").strip()
    response_id = data.get("response_id", "none")
    dilemma = data.get("dilemma", "unknown")

    print(f"{response_id}: {user_input} (Dilemma: {dilemma})")

    session_key = (response_id)
    now = time.time()

    # Reset session if new or timed out
    if (
        session_key not in all_sessions
        or now - all_sessions[session_key]["last_active"] > SESSION_TIMEOUT_SECONDS
    ):
        system_prompt = (
            "You are a nonjudgmental assistant helping the user resolve a dilemma.Keep replies short (3–5 sentences), plain language (~8th-grade). Ask clarifying questions if needed. "
                   )
        messages = [{"role": "system", "content": system_prompt}]
        all_sessions[session_key] = {"messages": messages, "last_active": now}
    else:
        messages = all_sessions[session_key]["messages"]

    messages.append({"role": "user", "content": user_input})
    print(messages)
    messages = trim_history(messages)
    bot_reply = "[Error: no response]"

    try:
        if client is None:
            bot_reply = "Error: OPENAI_API_KEY is not configured. Please add your OpenAI API key to Replit Secrets."
        else:
            resp = client.chat.completions.create(model=MODEL_NAME, messages=messages)
            content = resp.choices[0].message.content
            bot_reply = content.strip() if content else "[No response generated]"
            messages.append({"role": "assistant", "content": bot_reply})
    except Exception as e:
        bot_reply = f"Error generating response: {e}"

    # Update session
    all_sessions[session_key]["messages"] = messages
    all_sessions[session_key]["last_active"] = now
    system_prompt = all_sessions[session_key]["messages"][0]["content"]
    # --- Prepare record ---
    record = {
        "timestamp": datetime.datetime.now().isoformat(),
        "model": MODEL_NAME,
        "response_id": response_id,
        "system_prompt": system_prompt,
        "dilemma": dilemma,
        "user_input": user_input,
        "bot_reply": bot_reply,
    }

    # --- Save to CSV instead of JSONL ---
    csv_filename = "chatlog.csv"
    file_exists = os.path.isfile(csv_filename)

    with open(csv_filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "timestamp",
                "model",
                "response_id",
                "dilemma",
                "system_prompt",
                "user_input",
                "bot_reply",
            ],
        )
        if not file_exists:
            writer.writeheader()
        writer.writerow(record)

    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    # Run on port 5000 for Replit web preview (accessible via public URL)
    app.run(host="0.0.0.0", port=5000)
