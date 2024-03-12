import psycopg2
from dotenv import load_dotenv
import os

import views.add_product


def connection():
    try:

        conn = psycopg2.connect(
            dbname=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=os.getenv("DATABASE_POST")
        )

        return conn
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
    return []

def add_product(product):

    sql = "INSERT INTO products ( name, price, quantity, EAN, categories ) VALUES ( %s, %s, %s, %s, %s )"

    values = ( product['name'], product['price'], product['quantity'], product['ean'], product['category'] )

    conn = connection()

    cur = conn.cursor()

    cur.execute(sql, values)

    conn.commit()

    cur.close()

    conn.close()

    views.add_product.add_more_product_screen()




def edit_product(new_quantity, product_id):

    sql = "UPDATE products SET quantity = %s WHERE product_id = %s"

    values = ( new_quantity, product_id )

    connection(sql, values)

def get_products():

    sql = "SELECT * FROM products"

    conn = connection()

    cur = conn.cursor()

    cur.execute(sql)

    products = cur.fetchall()

    cur.close()

    conn.close()

    return products

def get_product_quantity_by_name( product_name ):

    sql = "SELECT quantity FROM products WHERE name = %s"

    conn = connection()

    cur = conn.cursor()

    cur.execute(sql, (product_name,) )

    product_quantity = cur.fetchall()

    if product_quantity:
        product_quantity = product_quantity[0][0]
    else:
        product_quantity = []

    cur.close()

    conn.close()

    return product_quantity