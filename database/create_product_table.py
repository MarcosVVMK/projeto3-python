import os, psycopg2
from dotenv import load_dotenv

def run():

    load_dotenv("../.env")

    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_POST")
        )
        cursor = conn.cursor()

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                product_id SERIAL PRIMARY KEY,
                name text,
                price decimal(10,2) not null,
                quantity integer,
                EAN text,
                categories text) """)

        conn.commit()

    except psycopg2.Error as e:
        print("Error in table creation:", e)
    finally:

        if conn is not None:
            conn.close()


run()