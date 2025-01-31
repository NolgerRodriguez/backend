from flask import Flask, request
from flask_cors import CORS
from whatsapp import send_message
from webhook import handle_webhook
from db import get_Chats, get_conversation

app = Flask(__name__)
CORS(app)

# Ruta para el webhook
@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    return handle_webhook()

# Ruta para enviar un mensaje a WhatsApp
@app.route("/send_message", methods=['POST'])
def send_message_route():
    data = request.json
    phone_number = data['phone_number']
    message = data['message']
    response = send_message(phone_number, message)
    return response

# Ruta para obtener datos de los chats
@app.route("/get_chats", methods=['GET'])
def get_chats_route():
    return get_Chats()

# Ruta para obtener una conversación
@app.route("/get_conversation/<number>", methods=['GET'])
def get_conversation_route(number):
    return get_conversation(number)

if __name__ == '__main__':
    app.run(port=5000, debug=True)