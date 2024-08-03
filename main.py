import os
from dotenv import load_dotenv
import psycopg2
import views.home

def main():
    load_dotenv(".env")
    
    # Conectar ao banco de dados usando variáveis de ambiente
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT")
        )
        print("Conexão ao banco de dados bem-sucedida!")




    except Exception as error:
        print("Erro ao conectar ao banco de dados:", error)

    views.home.home_screen()

if __name__ == '__main__':
    main()
