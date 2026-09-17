import sqlite3

connection = sqlite3.connect("../data/database.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                amount INTEGER NOT NULL
                )""")

def add_product(name, price=0, amount=0):
    cursor.execute("""
        INSERT INTO products (name, price, amount)
        VALUES (?, ?, ?)
    """, (name, price, amount))
    connection.commit()

def remove_product(id):
    cursor.execute("""
    SELECT name FROM products WHERE id = ?
    """, (id,))
    name = cursor.fetchall()
    print(name)
    cursor.execute("""
        DELETE FROM products WHERE id = ?
    """, (id,))
    connection.commit()

def get_product(id):
    cursor.execute("""
    SELECT * FROM products WHERE id = ?
    """, (id,))
    product = cursor.fetchall()
    print(product)



# cursor.execute("""SELECT * FROM products""")
# produtos = cursor.fetchall()
# print(produtos)
# for product in produtos:
#     id, name, price, amount = product
#     print(f"""ID: {id}
#     NOME: {name}
#     PREÇO: {price}
#     QUANTIDADE: {amount}
# """)



