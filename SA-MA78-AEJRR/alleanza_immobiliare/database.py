import os
import mysql.connector
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o sistema
load_dotenv()

def conectar():
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        # Como a porta geralmente é lida como string, convertemos para int
        port=int(os.getenv("DB_PORT")) 
    )
    
    return conexao