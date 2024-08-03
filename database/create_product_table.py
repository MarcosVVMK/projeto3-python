from calendar import c
import os
import psycopg2
from dotenv import load_dotenv

def run():
    create_database()
    create_table()

def create_database():
    load_dotenv("../.env")

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT")
        )

        # Ativar o modo autocommit
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname = '{}'".format(os.getenv("DATABASE_NAME")))

        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE {}".format(os.getenv("DATABASE_NAME")))
        
    except psycopg2.Error as e:
        print("Error in database creation:", e)

    finally:
        if conn is not None:
            conn.close()

def create_table():
    load_dotenv("../.env")

    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_PORT")
        )

        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            name TEXT UNIQUE,
            price DECIMAL(10,2) NOT NULL,
            quantity INTEGER,
            EAN TEXT,
            categories TEXT)
        """)

        conn.commit()

    except psycopg2.Error as e:
        print("Error in table creation:", e)

    finally:
        if conn is not None:
            conn.close()