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
    name = cursor.fetchone()
    cursor.execute("""
        DELETE FROM products WHERE id = ?
    """, (id,))
    connection.commit()
    print(f"Produto \"{name[0]}\" deletado com sucesso!")

def get_product_data(id):
    cursor.execute("""
    SELECT * FROM products WHERE id = ?
    """, (id,))
    return cursor.fetchone()

def format_product(product):
    id, name, price, amount = product

    return f"""
ID: {id}
Nome: {name}
Preço: R$ {price:.2f}
Quantidade: {amount}
"""

def get_total(id):
    product = get_product_data(id)
    id, name, price, amount = product
    total = price * amount
    return total


def get_product(id):
    product = get_product_data(id)

    if not product:
        print("Produto não encontrado.")
        return

    print(format_product(product))


def edit_product(id):
    product = get_product_data(id)

    if not product:
        print("Produto não encontrado.")
        return

    id, name, price, amount = product

    print(name)
    name = input("Digite o nome novo: ")

    print(price)
    price = float(input("Digite o preço novo: "))

    print(amount)
    amount = int(input("Digite a quantidade nova: "))

    cursor.execute("""
        UPDATE products
        SET name = ?, price = ?, amount = ?
        WHERE id = ?
    """, (name, price, amount, id))

    connection.commit()

    updated_product = get_product_data(id)
    print(format_product(updated_product))

def get_all_products():
    cursor.execute("""
        SELECT * FROM products
    """)

    return cursor.fetchall()


def order_by(column="id", direction="ASC"):
    allowed_columns = ["id", "name", "price", "amount"]
    allowed_directions = ["ASC", "DESC"]

    if column not in allowed_columns:
        print("Coluna inválida.")
        return []

    if direction not in allowed_directions:
        print("Direção inválida.")
        return []

    cursor.execute(f"""
        SELECT * FROM products
        ORDER BY {column} {direction}
    """)

    return cursor.fetchall()

def search_product(name):
    cursor.execute("""
        SELECT * FROM products
        WHERE name LIKE ?
    """, (f"%{name}%",))

    return cursor.fetchall()


