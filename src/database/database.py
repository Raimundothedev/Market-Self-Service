import sqlite3


connection = sqlite3.connect("../data/database.db")
cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price FLOAT NOT NULL,
        amount INTEGER NOT NULL
    )
""")