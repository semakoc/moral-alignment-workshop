# Moral Dilemma Chatbot (Replit Version)

> **Note:** This version is specifically adapted to run on **Replit**, removing all AWS, Cloudflare tunnel, and database dependencies in favor of a simple, reproducible setup.

This repository contains a lightweight, fully self‑contained web chatbot designed to support moral reflection in research, classroom, and workshop settings. It uses OpenAI’s `gpt-4o-mini` model for conversational reasoning and logs all interactions locally to a CSV file for later analysis.

## 🎯 What This Project Is For

The design prioritizes clarity, transparency, and ease of replication over scalability. It is well suited for:

* **Research Studies:** Conducting studies on moral reasoning or moral alignment.
* **Intervention Experiments:** AI‑mediated reflection tasks.
* **Qualtrics Integration:** Embedding an interactive chatbot inside Qualtrics surveys.
* **Education:** Live classroom demonstrations or workshops.
* **Prototyping:** Rapid prototyping without complex cloud infrastructure.

---

## 📂 Project Structure
.
├── chatbot.py        # Flask backend + OpenAI calls
├── chat.html         # Frontend chat interface
├── chatlog.csv       # Auto‑generated conversation log
├── requirements.txt  # Python dependencies
├── .replit           # Replit run configuration
├── pyproject.toml    # (Optional) Poetry/UV config
└── uv.lock           # (Optional) Lock file

***

### Section 2: Tech Stack and Setup Options

## 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | HTML, CSS, JavaScript (`chat.html`) |
| **Backend** | Python + Flask (`chatbot.py`) |
| **Model** | OpenAI `gpt-4o-mini` |
| **Storage** | Local CSV logging (inside Replit) |
| **Hosting** | Replit (Free tier supported) |


## 🚀 Running the Project on Replit

This project is designed to work out of the box on Replit.

### Option 1: Remix the Existing Repl (Recommended)
Use the working replication directly. Click "Remix" to create your own editable copy:
👉 **[Click here to Remix](https://replit.com/@kocse/moral-alignment-workshop?v=1)**

### Option 2: Manual Setup
1. Create a free account at [Replit.com](https://replit.com).
2. Click **Create Repl** → Choose **Python**.
3. Upload the following files from this repository into the repl:
    * `chatbot.py`
    * `chat.html`
    * `requirements.txt`
    * `.replit`

## Section 3: Environmental Variables
## 🔑 Environment Variables (Required)

Replit does not use `.env` files. Secrets must be added through the Replit interface.

1. Go to the Replit sidebar (left side of the workspace).
2. Click **Tools** (if needed) and select **Secrets** (Lock icon).
3. Add the following secrets:

| Key | Value |
| :--- | :--- |
| `OPENAI_API_KEY` | **(Required)** Paste your OpenAI API key here. |
| `OPENAI_MODEL` | **(Optional)** `gpt-4o-mini` (Defaults to this if omitted). |

> **Security Note:** These values are injected securely at runtime and are never exposed in the code or committed to GitHub.

## Section 4: Embedding in Qualtrics
## 🧩 Embedding in Qualtrics

The chatbot can be embedded directly inside a Qualtrics survey using an `iframe`. It accepts dynamic URL parameters to link survey data to chat logs.

### 1. URL Parameters
The chatbot reads the following parameters from the URL:
* `participant_id`: Participant identifier.
* `response_id`: Qualtrics response ID.
* `dilemma`: The specific moral dilemma text or ID.

### 2. Integration Steps
1. In Qualtrics, create a **Descriptive Text** question.
2. Click the text box → **Rich Content Editor**.
3. Switch to **HTML View** (`<>` icon or "Source").
4. Paste the following code:

```html
<iframe
  src="[https://your-project-name.username.repl.co/?participant_id=$](https://your-project-name.username.repl.co/?participant_id=$){e://Field/participant_id}&response_id=${e://Field/ResponseID}&dilemma=${q://QID116/ChoiceGroup/SelectedChoices}"
  width="100%"
  height="700"
  style="border:1px solid #ccc; border-radius:8px;">
</iframe>
5. Configuration
* Replace URL: Change your-project-name.username.repl.co with your actual Replit webview URL.

*Replace QID: Change QID116 to the specific Qualtrics Question ID that holds the dilemma text.

***

### Section 5: Logs, Troubleshooting, and Attribution

```markdown
## 📊 Viewing and Downloading Logs

No database setup is required. All conversations are automatically appended to `chatlog.csv` inside the file tree.

**Columns Logged:**
`timestamp` | `model` | `participant_id` | `response_id` | `dilemma` | `user_input` | `bot_reply`

**To Access Data:**
* Open the file directly inside the Replit editor.
* Download the file for analysis in R, Python, Excel, or Stata.

---

## ⚠️ Troubleshooting

If clicking **Run** does nothing or the app fails to start, check the following:

### 1. Run button does nothing / Exits immediately
Check your `.replit` file. It must contain this exact line:
```toml
run = "python3 chatbot.py"

## 📝 Author and Attribution

**Developed for the FutureUS / Moral Alignment Workshop**

* **Sema Koc**
* Mortality Lab
* Boston College

---

### License
This project is intended for **research and educational use**.
You may remix, adapt, and extend it for academic workshops or studies with appropriate attribution.
