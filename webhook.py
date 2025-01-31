from flask import request
from db import user_message, get_conversation, new_conversation

def handle_webhook():
    if request.method == 'GET':
        # Verificacion del webhook
        verify_token = "mATd5FNRnQokNRfyVy6KvW"
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        # Devolviendo la verificación
        if mode == 'subscribe' and token == verify_token:
            print('Webhook verificado.')
            return challenge, 200
        else:
            print('Webhook no verificado.')
            return 'Webhook no verificado.', 403
    
    elif request.method == 'POST':
        # Procesar mensajes entrantes
        data = request.json
        try:
            # Extraer los valores
            entry = data['entry'][0]
            change = entry['changes'][0]
            value = change['value']

            # Ignorar si el evento no contiene mensajes
            if 'messages' not in value:
                return 'EVENT_RECEIVED', 200

            # Procesar mensajes entrantes
            message = value['messages'][0]
            from_id = message['from']  # ID del remitente
            message_id = message['id']  # ID del mensaje
            timestamp = message['timestamp']  # Timestamp
            text_body = message['text']['body']  # Texto del mensaje
            msg_type = message['type']  # Tipo de mensaje


            if get_conversation(from_id) is None:
                new_conversation(from_id)
                user_message(from_id, text_body, message_id, "ON", msg_type, timestamp)
            else:
                user_message(from_id, text_body, message_id, "ON", msg_type, timestamp)
            
        except Exception as e:
            print(f"Error procesando el webhook: {e}")
            return 'ERROR', 500

    return 'EVENT_RECEIVED', 200

