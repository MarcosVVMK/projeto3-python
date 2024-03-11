import psycopg2
from dotenv import load_dotenv
import os


# TODO: create a seed to generate database rows
def connection(sql, values):

    load_dotenv("../.env")
    query = ""

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

        conn.commit()
        cur.close()
        conn.close()


    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)

    return query

def add_product(product):

    sql = "INSERT INTO products ( name, price, quantity, EAN, categories ) VALUES ( %s, %s, %s, %s, %s )"
    values = ( product['name'], product['price'], product['quantity'], product['EAN'], product['categories'] )

    connection( sql, values )


def edit_product(new_quantity, product_id):

    sql = "UPDATE products SET quantity = %s WHERE product_id = %s"
    values = ( new_quantity, product_id)

    connection(sql, values)

def get_products():

    sql = "SELECT * FROM product"

    products = connection(sql, "")

    return products

def get_product_quantity_by_name( product_name ):

    sql = "SELECT quantity FROM product WHERE product_name = %s"

    product = connection(sql, product_name)

    if product is None:
        return None
    else:
        return product['quantity']