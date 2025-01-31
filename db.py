import mysql.connector
from datetime import datetime

def get_db_conversation():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Conversaciones"
    )

# Función para crear una nueva conversación
# Recibe el nombre de la tabla que será el número de WhatsApp
def new_conversation(table_name):
    connection = get_db_conversation()
    cursor = connection.cursor()
    query = f"""
    CREATE TABLE `{table_name}` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `user_number` BIGINT NOT NULL,
        `message` TEXT NOT NULL,
        `message_id` TEXT NOT NULL,
        `type` TINYTEXT NOT NULL,
        `state` TINYTEXT NOT NULL DEFAULT 'ON',
        `timestamp` TINYTEXT NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE = InnoDB;
    """
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

# Función para eliminar una conversación
# Recibe el nombre de la tabla que será el número de WhatsApp
def delete_conversation(table_name):
    try:
        connection = get_db_conversation()
        cursor = connection.cursor()
        query = f"DROP TABLE `{table_name}`"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    except:
        print("No se pudo eliminar la conversacion")
        pass

# Función para obtener una conversación
# Recibe el nombre de la tabla que será el número de WhatsApp
def get_conversation(table_name):
    try:
        connection = get_db_conversation()
        cursor = connection.cursor()
        query = f"SELECT * FROM `{table_name}`"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    except:
        return None

# Función para insertar un mensaje del bot en una conversación
def admin_message(to ,message):
    type = "TXTbot"
    user_number = 0
    message_id = 0
    state = "ON"
    dt = datetime.now()
    timestamp = int(datetime.timestamp(dt))
    connection = get_db_conversation()
    cursor = connection.cursor()
    query = f"INSERT INTO `{to}` (user_number, message, message_id, type, state, timestamp) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (user_number, message, message_id, type, state, timestamp))
    connection.commit()
    cursor.close()
    connection.close()

# Función para obtener todas las conversaciones
def get_Chats():
    connection = get_db_conversation()
    cursor = connection.cursor()
    query = "SHOW TABLES"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

# Función para insertar un mensaje de un usuario en una conversación
def user_message(user_number, message, message_id, type, state, timestamp):
    if user_number is None:
        user_number = 0
    try:
        connection = get_db_conversation()
        cursor = connection.cursor()
        query = f"INSERT INTO `{user_number}` (user_number, message, message_id, type, state, timestamp) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (user_number, message, message_id, type, state, timestamp))
        connection.commit()
        cursor.close()
        connection.close()
    except:
        print("No se pudo insertar el mensaje en la conversacion")
        pass