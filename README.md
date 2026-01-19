# Moral Alignment Chatbot (Replit Version)

> **Note:** This version is specifically adapted to run on **Replit**, removing all AWS, Cloudflare tunnel, and database dependencies in favor of a simple, reproducible setup.

This repository contains a lightweight, fully self‑contained web chatbot designed to support moral reflection in research, classroom, and workshop settings. It uses OpenAI’s `gpt-4o-mini` model for conversational reasoning and logs all interactions locally to a CSV file for later analysis.

### 🎯 What This Project Is For

This GitHub repository was created to accompany the professional development session Building Free-Form Data Pipelines for Human-AI Conversations in Surveys, delivered at the SPSP 2026 Annual Convention in Chicago, IL. The project supports the workshop by providing a concrete, runnable example of how free-form human–AI conversations can be embedded in surveys and logged through a flexible data pipeline.

**You do not need prior programming experience to follow the workshop or run the demo version of this project.
**
The implementation uses a moral reasoning chatbot drawn from Moral Reasoning with AI Chatbots in Naturalistic Conversation: Choices, Perceptions, and Value Alignment as a demonstration case. The moral reasoning task is included to make the data pipeline concrete and interpretable, rather than to present substantive research findings.

This Replit-based version is designed for education, demonstration, and rapid prototyping. **While Replit offers an accessible environment for workshops and teaching, it is not recommended for formal research data collection involving sensitive participant information.** For production research deployments, we advise using AWS or other secure cloud servers that provide stronger data security, access controls, and compliance support.

---
## Section 1: Structure, Tech Stack, Deployment
### 📂 Project Structure
**Most users only need to interact with backend.py and frontend.html. The other files support setup and logging.**

Project files:

`backend.py`
- What it does: Runs the chatbot logic and communicates with the OpenAI API.
- Used where: Uploaded to Replit.
- Notes: This is the main file that Replit runs when you click “Run.”

`frontend.html`
- What it does: Displays the chat interface that participants interact with.
- Used where: Uploaded to Replit and embedded into Qualtrics using an iframe.
- Notes: This file controls the layout and appearance of the chatbot.

`chatlog.csv`
- What it does: Stores all chatbot conversations.
- Used where: Automatically generated in Replit.
- Notes: You do not upload this file. It appears after the chatbot runs.

`requirements.txt`
- What it does: Lists the Python packages required to run the chatbot.
- Used where: Uploaded to Replit.
- Notes: Replit automatically installs these packages when the project runs.

`.replit`
- What it does: Tells Replit how to start the app.
- Used where: Uploaded to Replit.
- Notes: This file specifies which Python file to run.

### 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | HTML, CSS, JavaScript (`frontend.html`) |
| **Backend** | Python + Flask (`backend.py`) |
| **Model** | OpenAI `gpt-4o-mini` |
| **Storage** | Local CSV logging (inside Replit) |
| **Hosting** | Replit (Free tier supported) |


### 🚀 Running the Project on Replit

This project is designed to work out of the box on Replit.

### Option 1: Remix the Existing Repl (Recommended)
Use the working replication directly. Click "Remix" to create your own editable copy:
👉 **[Click here to Remix](https://replit.com/@kocse/moral-alignment-workshop?v=1)**

### Option 2: Manual Setup
1. Create a free account at [Replit.com](https://replit.com).
2. Click **Create Repl** → Choose **Python**.
3. Upload the following files from this repository into the repl:
    * `backend.py`
    * `frontend.html`
    * `requirements.txt`
    * `.replit`

## Section 2: Environmental Variables
### 🔑 Environment Variables (Required)

This project requires an OpenAI API key to run. The API key allows the chatbot to send messages to the OpenAI model.

### How to Get an OpenAI API Key
1. Go to the OpenAI API keys page:
https://platform.openai.com/settings/organization/api-keys
2. Sign in using an OpenAI account or create one using your Google account.
3. Create a new API key and copy it.
Important:
This API key is not the same as your ChatGPT login. Having access to ChatGPT does not automatically give you an API key.
Note:
No credit card is required to create an API key for basic usage.

### Adding the API key in Replit
1. Go to the Replit sidebar (left side of the workspace).
2. Click **Tools** (if needed) and select **Secrets** (Lock icon).
3. Add the following secrets:

| Key | Value |
| :--- | :--- |
| `OPENAI_API_KEY` | **(Required)** Paste your OpenAI API key here. |
| `OPENAI_MODEL` | **(Optional)** `gpt-4o-mini` (Defaults to this if omitted). |

> **Security Note:** These values are injected securely at runtime and are never exposed in the code or committed to GitHub.

## Section 3: Embedding in Qualtrics
### 🧩 Embedding in Qualtrics

You can embed the chatbot in a Qualtrics survey using an iframe. Qualtrics will display the chatbot, while the chatbot itself runs on Replit.

To connect survey metadata (like participant ID and response ID) to your chat logs, Qualtrics passes values into the chatbot through the iframe URL.

### Step 1: Create the Qualtrics feilds (particpant_id and response_id)
Qualtrics needs values to send into the chatbot. The simplest way is to use Embedded Data.

1. In Qualtrics, open your survey.
2. Go to Survey Flow.
3. Click Add a New Element Here → choose Embedded Data.
4. Add these fields (exact names recommended):
   * participant_id
   * response_id
5. Set the values:
   * If you already have a participant ID from recruitment software, set `participant_id` to that value (often via piped text).
   * Set response_id to Qualtrics’ built-in Response ID using piped text:
`response_id = ${e://Field/ResponseID}`
6. Click Apply Flow.
Notes:
   * If you do not have a participant ID source, you can still run the chatbot using only response_id.
   * The field names matter because the chatbot expects these parameter names.

### Step 2: Put the dilemma text in a question
The chatbot can also receive a dilemma through the URL parameter `dilemma`.
1. Add a question that contains the dilemma content (many people use Descriptive Text).
2. This “dilemma question” should appear before the chatbot question, so participants see the dilemma first.

Important: Qualtrics will assign that dilemma question an internal ID like QID116. You will use that ID in the iframe code.

### Step 3:Find the dilemma question ID (the “QID”)
You need the Qualtrics Question ID for the question that contains the dilemma text.
Common ways to find it:
* In the survey editor, click the dilemma question and look for its question ID (often visible in the question settings or the browser address bar URL).
* Use Qualtrics’ preview link and inspect the page source for QID### (more technical).

Once you find it, you will replace QID116 in the example code with your dilemma question’s actual ID.

### Step 4:Get your Replit URL (what the iframe points to)
Your iframe must point to the public web URL of your running Replit app.
1. Open your Replit project.
2. Click **Run**.
3. When the app opens in the Replit webview, find the “open in new tab” option (or copy the URL from the webview).
4. The URL will look like: `https://your-repl-name.username.repl.co`
You will paste this URL into the iframe src.

Important: The iframe points to the Replit app URL, not to filenames like `frontend.html` or `backend.py`.

### Step 5: Add the iframe question in Qualtrics
1. Add a Descriptive Text question where you want the chatbot to appear.
2. Click the text box → Rich Content Editor.
3. Switch to HTML View (the <> icon).
4. Paste the iframe code below.

```html
<iframe
  src="https://your-repl-name.username.repl.co/?participant_id=$(https://your-project-name.username.repl.co/?participant_id=$){e://Field/participant_id}&response_id=${e://Field/ResponseID}&dilemma=${q://QID116/ChoiceGroup/SelectedChoices}"
  width="100%"
  height="700"
  style="border:1px solid #ccc; border-radius:8px;">
</iframe>
```

5. Configuration
* Replace URL: Change your-repl-name.username.repl.co with your actual Replit webview URL.
* Replace QID: Change QID116 to the specific Qualtrics Question ID that holds the dilemma text.

***

## Section 4: Logs, Troubleshooting, and Attribution

### 📊Viewing and Downloading Logs

No database setup is required. All conversations are automatically appended to `chatlog.csv` inside the file tree.

**Columns Logged:**
`timestamp` | `model` | `participant_id` | `response_id` | `dilemma` | `user_input` | `bot_reply`

**To Access Data:**
* Open the file directly inside the Replit editor.
* Download the file for analysis in R, Python, Excel, or Stata.

---

### ⚠️Troubleshooting
If clicking **Run** does nothing or the app fails to start, check the following:
Check your `.replit` file. It must contain this exact line:
```toml
run = "python3 backend.py"
```
### 📝Author and Attribution

This project was developed as part of work associated with the Morality Lab and the SPSP 2026 professional development session _Building Free-Form Data Pipelines for Human-AI_ Conversations in Surveys.

**Authors:**

* Helen H. Zheng
* Sara Haman
* Sema Koc

**Affiliation:**

Morality Lab, Boston College

**Attribution guidance:**

This repository may be remixed or adapted for research, educational, or workshop use. Please cite the SPSP 2026 presentation and acknowledge the Morality Lab when using or extending this codebase.

**APA Citation**:
Zheng, H. H., Haman, S., & Koc, S. (2026, February 27). Building Free-Form Data Pipelines for Human-AI Conversations in Surveys. SPSP 2026 Annual Convention.

### License
This project is intended for research and educational use.
You may remix, adapt, and extend it for academic workshops or studies with appropriate attribution.
