"""
Groq Chatbot API Wrapper
A simple chatbot API that uses Groq for responses.

Receives: {"message": "hello"}
Returns: {"response": "AI response from Groq"}
"""

from flask import Flask, request, jsonify, send_from_directory
from groq import Groq
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# Lazy load Groq client
groq_client = None

def get_groq_client():
    global groq_client
    if groq_client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        groq_client = Groq(api_key=api_key)
    return groq_client

# System prompt for the chatbot
SYSTEM_PROMPT = """You are a helpful customer service assistant for a tech company.
You help users with:
- Product information and features
- Pricing and plans
- Technical support
- General inquiries

Be friendly, professional, and concise in your responses."""


@app.route('/chat', methods=['POST'])
def chat():
    """
    Chat endpoint
    POST /chat
    Body: {"message": "user message here"}
    Response: {"response": "bot response"}
    """
    try:
        # Get user message
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        
        # Call Groq API
        chat_completion = get_groq_client().chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model="llama-3.3-70b-versatile",  # Fast and good quality
            temperature=0.7,
            max_tokens=500,
        )
        
        # Extract response
        bot_response = chat_completion.choices[0].message.content
        
        return jsonify({"response": bot_response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok", "message": "Groq chatbot is running"})


@app.route('/', methods=['GET'])
def index():
    """Serve the chatbot UI"""
    return send_from_directory('.', 'index.html')


if __name__ == '__main__':
    # Check if API key is set
    if not os.getenv("GROQ_API_KEY"):
        print("=" * 50)
        print("⚠️  ERROR: GROQ_API_KEY not set!")
        print("=" * 50)
        print()
        print("Set it with:")
        print("  set GROQ_API_KEY=your_key_here")
        print()
        print("Get free key: https://console.groq.com/keys")
        print("=" * 50)
        exit(1)
    
    print("=" * 50)
    print("🤖 Groq Chatbot API Server")
    print("=" * 50)
    print()
    print("Endpoints:")
    print("  POST http://localhost:5000/chat")
    print("  GET  http://localhost:5000/health")
    print()
    print("Example request:")
    print('  curl -X POST http://localhost:5000/chat \\')
    print('       -H "Content-Type: application/json" \\')
    print('       -d \'{"message": "Hello!"}\'')
    print()
    print("Press Ctrl+C to stop")
    print("=" * 50)
    print()
    
    app.run(host='0.0.0.0', port=5000, debug=False)