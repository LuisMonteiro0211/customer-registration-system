from mysql.connector import connect, Error
from dotenv import load_dotenv
from pathlib import Path
from contextlib import contextmanager
import os
import logging

load_dotenv() # Carrega as variáveis de ambiente do arquivo .env

@contextmanager
def get_connection():
    connection = None
    cursor = None

    try:
        connection = connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT'))
        )
        cursor = connection.cursor()
        logging.info(f"Conexão estabelecida com sucesso! Cursor: {cursor}")
        yield cursor
        connection.commit()

    except Error as error:
        if connection is not None:
            connection.rollback()
        raise error # Re-lança o erro para ser tratado pelo chamador

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

if __name__ == "__main__":
    # Testa a conexão com o banco de dados
    connection = get_connection()
