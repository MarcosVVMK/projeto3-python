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


        create_products_table(cursor)
        create_users_table(cursor)
        create_users_sales(cursor)

        conn.commit()

    except psycopg2.Error as e:
        print("Error in table creation:", e)
    finally:

        if conn is not None:
            conn.close()



def create_products_table(cursor):

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
        product_id integer PRIMARY KEY,
        name text,
        price text,
        quantity integer,
        EAN integer,
        categories text) """ )



    return print("creating product table")


def create_users_table( cursor ):

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        user_id integer PRIMARY KEY,
        name text,
        email text,
        telefone text,
        senha text ) """)

    return print("creating users table")

def create_users_sales( cursor ):

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
        sales_id integer PRIMARY KEY,
        product_id integer,
        user_id integer, 
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        sale_total_price decimal(10,2) not null ) """)

    return print("creating sales table")



run()