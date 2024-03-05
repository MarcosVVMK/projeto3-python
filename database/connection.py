import psycopg2
from dotenv import load_dotenv
import os


# TODO: create a seed to generate database rows
def connection(sql, values):

    load_dotenv("../.env")

    try:

        conn = psycopg2.connect(
            dbname=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_POST")
        )

        cur = conn.cursor()

        query = cur.execute(sql, values)

        cur.close()
        conn.close()


    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)


def add_product(product):

    sql = "INSERT INTO products ( name, price, quantity, EAN, categories ) VALUES ( %s, %s, %s, %s, %s )"
    values = ( product['name'], product['price'], product['quantity'], product['EAN'], product['categories'] )

    connection( sql, values )


def edit_product(quantity, product_id):

    sql = "UPDATE products SET quantity = %s WHERE product_id = %s"


    connection(sql, values)