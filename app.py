from flask import Flask, request
from chatbot_logic import handle_message
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        print("📩 Received webhook payload:", data)

        user_message = data.get('message', '')
        user_id = data.get('sender_id', '')

        if not user_message:
            return {'error': 'Message is required'}, 400

        reply = handle_message(user_id, user_message)
        print("💬 Generated reply:", reply)

        return {'reply': reply}, 200
    except Exception as e:
        print("❌ Error occurred:", str(e))
        return {'error': str(e)}, 500

@app.route('/')
def home():
    return "Esoteric Chatbot is running."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
