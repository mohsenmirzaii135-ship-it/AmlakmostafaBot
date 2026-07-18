print("database.py loaded")
import sqlite3

DB_NAME = "houses.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS houses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        house_type TEXT,
        price INTEGER,
        area INTEGER,
        rooms INTEGER,
        location TEXT,
        description TEXT,
        photo TEXT,
        link TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_house(house_type, price, area, rooms, location, description, photo, link):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO houses
    (house_type, price, area, rooms, location, description, photo, link)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        house_type,
        price,
        area,
        rooms,
        location,
        description,
        photo,
        link
    ))

    conn.commit()
    conn.close()

def search_price(min_price, max_price):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM houses
    WHERE price >= ? AND price <= ?
    ORDER BY price
    """, (min_price, max_price))

    rows = cur.fetchall()

    conn.close()
    return rows

create_table()