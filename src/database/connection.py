from mysql.connector import connect, Error
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv() # Carrega as variáveis de ambiente do arquivo .env

def get_connection():
    try:
        connection = connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT'))
        )   
        return connection

    except Error as error:
        raise error # Re-lança o erro para ser tratado pelo chamador


if __name__ == "__main__":
    # Testa a conexão com o banco de dados
    connection = get_connection()
