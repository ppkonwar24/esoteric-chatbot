from flask import Flask, request
from chatbot_logic import handle_message

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    user_message = data.get('message', '')
    user_id = data.get('sender_id', '')
    reply = handle_message(user_id, user_message)
    return {'reply': reply}, 200

@app.route('/')
def home():
    return "Esoteric Chatbot is running."

if __name__ == '__main__':
    app.run(debug=True)
