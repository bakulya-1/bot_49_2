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
    photo TEXT,
    product_id TEXT
    )
"""

INSERT_store_query = """
    INSERT INTO store (name_product, size, price, photo, product_id)
    VALUES (?, ?, ?, ?, ?)
"""


CREATE_TABLE_store_detail = """
    CREATE TABLE IF NOT EXISTS store_detail(
    id INTEGER PRIMARY KEY AUTOUINCREMENT,
    product_id TEXT,
    category TEXT,
    info_product TEXT
    )
"""

INSERT_store_detail_query = """
    INSERT INTO store_detail (product_id, category, infop_roduct)
    VALUES (?, ?, ?)
"""


CREATE_TABLE_collections = """
    CREATE TABLE IF NOT EXISTS collections(
    id INTEGER PRIMARY KEY AUTOUINCREMENT,
    collection TEXT,
    product_id TEXT
    )
"""

INSERT_collections_query = """
    INSERT INTO collections (collection, product_id)
    VALUES (?, ?)
"""





