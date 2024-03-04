import os, sys
sys.path.insert(0, os.path.abspath(".."))
from database.connection import conn, cursor, close_connection

def run():


    create_products_table()
    #create_users_table()
    #create_users_sales()

    close_connection( conn() )


def create_products_table():
    cursor().execute("""
        CREATE TABLE IF NOT EXISTS products (
        product_id integer PRIMARY KEY,
        name text,
        price text,
        quantity integer,
        EAN integer,
        categories text
    )
    """)


    conn().commit()


def create_users_table():
    cursor().execute("""
        CREATE TABLE IF NOT EXISTS users (
        user_id integer PRIMARY KEY,
        name text,
        email text,
        telefone text,
        senha text
    )
    """)
    print("creating users table")
    conn().commit()

def create_users_sales(cur):
    cursor().execute("""
        CREATE TABLE IF NOT EXISTS sales (
        sales_id integer PRIMARY KEY,
        FOREIGN KEY (product_id) REFERENCES products(product_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        sale_total_price decimal(10,2) not null
    )
    """)
    print("creating sales table")
    conn().commit()


run()