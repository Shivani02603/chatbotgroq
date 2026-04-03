# 🚀 Groq Chatbot Deployment Guide

## Local Testing

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Environment Variable
```bash
# On Windows (PowerShell)
$env:GROQ_API_KEY = "your_groq_api_key_here"

# Or on Command Prompt
set GROQ_API_KEY=your_groq_api_key_here

# On Mac/Linux
export GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key: https://console.groq.com/keys

### 3. Run Locally
```bash
python chatbot.py
```

Visit: http://localhost:5000

---

## Deploy to Render (Recommended for Flask)

### Step 1: Push to GitHub
1. Create a new GitHub repository
2. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/groq-chatbot.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Render
1. Go to https://render.com/ and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Fill in the details:
   - **Name:** groq-chatbot
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn chatbot:app`
5. Add Environment Variable:
   - **Key:** `GROQ_API_KEY`
   - **Value:** Your Groq API key
6. Click "Create Web Service"
7. Wait for deployment (takes 2-5 minutes)
8. Get your public URL!

---

## Deploy to Vercel (Alternative)

Vercel is better for serverless functions, but not ideal for long-running Flask apps.
For best results, use Render (above).

---

## API Endpoints

### Chat Endpoint
```
POST /chat
Content-Type: application/json

{
  "message": "Hello!"
}

Response:
{
  "response": "AI generated response"
}
```

### Health Check
```
GET /health

Response:
{
  "status": "ok",
  "message": "Groq chatbot is running"
}
```

### Web UI
```
GET /
```
Open in browser to use the chatbot UI

---

## Troubleshooting

### "GROQ_API_KEY not set"
- Make sure you set the environment variable before running
- On Render, add it in the Environment Variables section

### "Connection refused"
- Check if the app is running with `python chatbot.py`
- Check the console for errors

### "Module not found"
- Make sure you installed dependencies: `pip install -r requirements.txt`

---

## Files Included

- `chatbot.py` - Flask API server with Groq integration
- `index.html` - Web UI for the chatbot
- `requirements.txt` - Python dependencies
- `Procfile` - Render deployment configuration
- `.gitignore` - Git ignore rules
