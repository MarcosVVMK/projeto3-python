import psycopg2
from dotenv import load_dotenv
import os


# TODO: create a seed to generate database rows
def connection():

    load_dotenv("../.env")
    try:

        conn = psycopg2.connect(
            dbname=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_POST")
        )

        print( "Connection established" )

        return conn

    except psycopg2.Error as e:

        print("Erro ao conectar ao banco de dados:", e)



