from itertools import product

CREATE_TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age TEXT,
    email TEXT,
    city TEXT,
    photo TEXT
    )
"""


INSERT_registered_query = """
    INSERT INTO registered (fullname, age, email, city, photo)
    VALUES (?, ?, ?, ?, ?)
"""


CREATE_TABLE_store ="""
    CREATE TABLE IF NOT EXISTS store(
    id INTEGER PRIMARY KEY AUTOUINCREMENT,
    name_product TEXT,
    size TEXT,
    price REAL,
    photo1 TEXT
    )
"""

INSERT_store_query = """
    INSERT INTO store (name_product, size, price, photo1, category)
    VALUES (?, ?, ?, ?, ?)
"""


CREATE_TABLE_products_details = """
    CREATE TABLE IF NOT EXISTS products_details(
    id INTEGER PRIMARY KEY AUTOUINCREMENT,
    productid INTEGER,
    category TEXT,
    infoproduct TEXT,
    FOREIGN KEY (productid) REFERENCES store(id)
    )
"""

INSERT_products_details_query = """
    INSERT INTO productid_details (productid, category, infoproduct)
    VALUES (?, ?, ?)
"""





