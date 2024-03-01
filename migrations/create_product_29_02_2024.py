from ..database import *

conn = connection.conn()

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS product (
    id integer PRIMARY KEY,
    name text,
    price text,
    quantity integer,
    categories text
)
""")
conn.commit()


conn.close()