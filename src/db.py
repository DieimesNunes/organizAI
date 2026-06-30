import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def conectar():
    """
    Cria uma conexão com o banco de dados PostgreSQL.
    As informações de conexão são carregadas do arquivo .env.
    """

    conexao = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return conexao