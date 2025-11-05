# Moral Dilemma Chatbot
A web-based chatbot designed to help users reflect on moral dilemmas. It uses OpenAI's GPT-4o for conversational reasoning and logs all interactions to AWS S3 for later analysis.

## Overview
This chatbot is ideal for the following uses:
- Research studies involving reflective interventions
- Embedding into Qualtrics surveys
- Lightweight deployments without databases

## Tech Stack
- **Front end:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Model:** OpenAI GPT-4o
- **Storage:** AWS S3 (CSV File Log)
- **Deployment:** EC2 + Cloudflare Tunnel

## How to use: Running on AWS EC2 (Recommended Setup)

This project is designed to be deployed on an AWS EC2 instance, connected with both a Qualtrics survey and a public-facing tunnel (Cloudflare used in this project).

### 1. Launch EC2 Instance

We recommend:
- **Instance type:** t2.medium or better
- **OS:** Amazon Linux 2 or Ubuntu 20.04
- **Ports:** Ensure port **5000** is allowed in your security group (for Flask), or use Cloudflare Tunnel to expose it securely

### 2. SSH into the Instance
```ssh -i your-key.pem ec2-user@your-ec2-public-ip```

### 3. Install Dependencies
```sudo yum update -y```
```sudo yum install python3 pip -y```

### 4. Install Python Packages
```pip install flask flask-cors boto3 openai```

### 5. Clone the Repository
```git clone https://github.com/lypsychlab/qualtrics-multiround-chatbot-integration.git```
```cd moral-dilemma-chat```

### 6. Configure API Key
In chatbot.py:
  Move to line 19 --> **client = OpenAI(api_key="...")**
  Replace "..." with your unique OpenAI API key

### 7. Start the Flask server locally (Run the app)
```python3 chatbot.py```

## Running the Chatbot in Parallel Using _screen_
We recommend using _screen_ to keep the chatbot and Cloudflare tunnel running in separate terminal sessions.

### Step-by-Step Setup
## Start the Flask App in One Screen
Start the Cloudflare Tunnel in Another Screen
```screen -s chatbot (screen name)```
```python 3 chatbot.py```

Then, press Ctrl+A, then D to detach from the screen and return to the home terminal

## Start the Cloudflare Tunnel in Another Screen
```screen -S tunnel```
```cloudflared tunnel --url http://localhost:5000 #Command to create tunnel```

This will generate a temporary URL like this:
"moral-walrus-sunset.trycloudflare.com"

## These are some useful commands to navigate in and out of your screens
- screen -ls            # list screens
- screen -r chatbot     # reattach chatbot
- screen -r tunnel      # reattach tunnel

Using screens allows for the tunnel and the Flask app to run continuously within one instance window. 

---

### Making It Public: Cloudflare Tunnel

Using a temporary Cloudflare tunnel allows the Flask app to be accessed publicly via a generated URL. A **new tunnel is created each time the command is run**, and a **new URL is assigned**.
- A new tunnel must be created each time the EC2 instance is restarted.
- However, if the instance remains running and the tunnel is started inside a persistent _screen_ session, the same tunnel will stay active.

To start a temporary tunnel:
  cloudflared tunnel --url http://localhost:5000

## Linking to Qualtrics
The chatbot is embedded inside a Qualtrics question's HTML, using an <iframe> element.

Since the Cloudflare tunnel URL changes each time it's created, you must update the iframe's src with the new URL before launching the survey.

Example iframe code:
  ```
<iframe 
    src="https://your-new-tunnel-url.trycloudflare.com?  participant_id=${e://Field/ProlificID}&response_id=${e://Field/ResponseID}&dilemma=${e://Field/Dilemma}" 
    width="100%" 
    height="600" 
    style="border:none;">
  </iframe>
  ```

This will:
- Embed the chatbot UI directly in the survey
- Pass participant metadata for session tracking and S3 logging
**Be sure the EC2 instance and Cloudflare tunnel are both running during survey deployment.
**


### Recommendation 
We recommend running this on AWS EC2 with S3 + OpenAI integration for full functionality, security, and scalability.

### Author
...
### Licence
...