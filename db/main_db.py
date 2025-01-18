
import sqlite3
from db import queries


db = sqlite3.connect('db/registered.sqlite3')
cursor = db.cursor()


async def create_db():
    if db:
        print('База данных подключена.')

    cursor.execute(queries.CREATE_TABLE_registered)


async def sql_insert_registered(fullname, age, email, city, photo):
    cursor.execute(queries.INSERT_registered_query, (
        fullname, age, email, city, photo
    ))

    db.commit()


db = sqlite3.connect('db/registered.sqlite3')
cursor = db.cursor()

async def create_db():
    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_products_details)
    await create_db()

    db.commit()


async def sql_insert_store(name, size, price, photo1, category):
    cursor.execute(queries.INSERT_store_query, (
        name, size, price, photo1, category
    ))
    db.commit()

    productid = cursor.lastrowid
    return productid

async def sql_insert_products_details(productid, category, infoproduct):
    cursor.execute(queries.INSERT_products_details_query, (
        productid, category, infoproduct
    ))
    db.commit()







