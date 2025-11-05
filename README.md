# Moral Dilemma Chatbot (Replit Version)

A lightweight web-based chatbot designed to help users reflect on moral dilemmas.  
It uses **OpenAI’s GPT-4o-mini** for conversational reasoning and logs all interactions to a **CSV file** inside Replit for later analysis.

---

## Overview

This chatbot is ideal for:

- Research studies involving moral reflection or AI-mediated interventions  
- Embedding within **Qualtrics surveys**  
- Classroom or workshop demonstrations of human–AI dialogue  
- Lightweight deployments without databases or cloud infrastructure  

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS, JavaScript (`chat.html`) |
| **Backend** | Python (Flask) |
| **Model** | OpenAI GPT-4o-mini |
| **Storage** | Local CSV logging (within Replit) |
| **Deployment** | Replit (free tier) |

---

## How to Run the Chatbot on Replit

This version is designed for simple, reproducible use inside **Replit**, which hosts both the backend (Flask) and frontend (HTML).  
No AWS, Cloudflare, or manual tunnels are required.

---

### 1. Open or Remix the Repl

You can **remix** (Replit’s term for “fork”) the working version using this link:

👉 [https://replit.com/@kocse/moral-alignment-workshop?v=1](https://replit.com/@kocse/moral-alignment-workshop?v=1)

Alternatively, you can import the project manually:

1. Go to [**replit.com**](https://replit.com) and create a free account.  
2. Click **Create Repl → Python**.  
3. Upload these files:  
   - `chatbot.py`  
   - `chat.html`  
   - `requirements.txt`  

---

### 2. Configure Secrets (Environment Variables)

In the Replit left sidebar, open **Tools → Secrets (🔒 icon)** and add:

| Name | Value |
|------|--------|
| `OPENAI_API_KEY` | your OpenAI API key |
| *(optional)* `OPENAI_MODEL` | `gpt-4o-mini` |

This keeps your key private and out of the code.

---

### 3. Check Your Run Configuration

Make sure Replit knows which file to run:

1. If a file named `.replit` exists, ensure it contains:

   ```toml
   run = "python3 chatbot.py"
2. Click Run (green button).
   Wait for the console to show: Running on http://0.0.0.0:80
3. Replit will open a Preview tab with a live URL like: https://your-project-name.username.repl.co/
   That’s your public chatbot URL.

### 4. Test It

1. Click **Run** (green button).  
2. Wait for the console to show: Running on http://0.0.0.0:80
3. Replit will open a **Preview** tab with a live URL like: https://your-project-name.username.repl.co/
   That’s your public chatbot URL.

---

### 5. Linking to Qualtrics

Embed the chatbot directly inside a Qualtrics survey (Descriptive Text → HTML view):

```html
<iframe
src="https://your-project-name.username.repl.co/?participant_id=${e://Field/participant_id}&response_id=${e://Field/ResponseID}&dilemma=${q://QID116/ChoiceGroup/SelectedChoices}"
width="100%"
height="700"
style="border:1px solid #ccc;border-radius:8px;">
</iframe>
```
## 6. Viewing and Downloading Logs

Each user message and AI reply is saved to **`chatlog.csv`** with the following columns:

| timestamp | model | participant_id | response_id | dilemma | user_input | bot_reply |
|------------|--------|----------------|--------------|----------|-------------|------------|

You can download this file directly from Replit for analysis in **R**, **Excel**, or **Python**.

---

## 7. Keeping the App Active During a Workshop

Replit free-tier projects sleep after inactivity. To keep it live during a session:

- Keep the Replit browser tab open, or  
- Enable **Always On** (available in paid plans)

Participants can **remix** the Repl, add their own OpenAI keys, and immediately use the **Preview** tab.

---

## Author

Developed for the **FutureUS / Moral Alignment Workshop**  
by Sema Koc, Mortality Lab, Boston College

---

## License

This project is for research and educational use.  
You may remix and adapt it for academic workshops or studies with appropriate citation.