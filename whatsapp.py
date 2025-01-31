import requests
from db import get_conversation, admin_message, new_conversation

# Configura tu token de acceso y número de WhatsApp desde la API de Meta
ACCESS_TOKEN = "EAANMh7tBkooBOxnGx6b8TWEMZCthVVIM6dbByFclQSZBCQeCmhAi6HEogxMvjiinCBU8erLJoWpMe8NRaT5AYjN3mgp3XZCvykDJm1zBkFDdt4f0CJu4EuJdjIZAmAcyLZClKTp2kjuqupTNXBnqDPaqLEL7RVXWBRZBP3hPiTqZBtcDWcSSmaZAz3Qf8BoSMRdgSQZDZD"
WHATSAPP_NUMBER_ID = "573042612549118"  # Reemplaza con tu ID de número de WhatsApp
GRAPH_API_URL = f"https://graph.facebook.com/v21.0/{WHATSAPP_NUMBER_ID}/messages"


# Función para enviar mensajes
def send_message(to, message):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    try:
        response = requests.post(GRAPH_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        if (get_conversation(to) == None):
            new_conversation(to)
            admin_message(to, message)
        else:
            admin_message(to, message)
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error al enviar el mensaje:", e)
        return {"error": str(e)}