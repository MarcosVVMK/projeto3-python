import psycopg2
from dotenv import load_dotenv
import os


# TODO: create a seed to generate db rows
def conn():

    load_dotenv("../.env")
    print("teste")
    return psycopg2.connect(
        dbname=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_POST")
    )