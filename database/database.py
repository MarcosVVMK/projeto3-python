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

def close_connection(conn, cur):
    cur.close()

    conn.close()


def verify_if_product_exist( product_name ):
    conn = connection()

    cur = conn.cursor()

    sql = "SELECT COUNT(*) FROM products WHERE name = %s"

    cur.execute(sql, (product_name,))

    rows = cur.fetchone()[0]

    close_connection(conn, cur)

    if rows > 0:
        return views.add_product.product_already_exists_screen()
    else:
        return



def add_product(product):

    sql = "INSERT INTO products ( name, price, quantity, EAN, categories ) VALUES ( %s, %s, %s, %s, %s )"

    values = ( product['name'], product['price'], product['quantity'], product['ean'], product['category'] )

    conn = connection()

    cur = conn.cursor()

    cur.execute(sql, values)

    conn.commit()

    close_connection(conn, cur)

    views.add_product.add_more_product_screen()


def edit_product(new_product_data):

    sql = "UPDATE products SET quantity = %s WHERE product_id = %s"

    values = ( new_product_data['quantity'], new_product_data['product_id'] )

    conn = connection()

    cur = conn.cursor()

    cur.execute(sql, values)

    conn.commit()

    close_connection(conn, cur)



def get_products():

    sql = "SELECT * FROM products"

    conn = connection()

    cur = conn.cursor()

    cur.execute(sql)

    products = cur.fetchall()

    close_connection(conn, cur)

    return products

def get_product_quantity_by_name( product_name ):
    product_data = {}

    sql = "SELECT quantity, product_id FROM products WHERE name = %s"

    conn = connection()

    cur = conn.cursor()

    cur.execute(sql, (product_name,) )

    query_response = cur.fetchall()

    if query_response:
        product_data['quantity'] = query_response[0][0]
        product_data['product_id'] = query_response[0][1]
    else:
        product_data = {}

    close_connection(conn, cur)

    return product_data