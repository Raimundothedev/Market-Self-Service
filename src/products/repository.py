from database.database import cursor, connection
from products.model import Product
import math as m


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

    product = cursor.fetchone()

    if not product:
        return False

    cursor.execute("""
        DELETE FROM products WHERE id = ?
    """, (id,))

    connection.commit()

    return True

def add_discount(id, discount: float):
    if 0 > discount > 100:
        return
    product = get_product_data(id)
    price = product.price

    f_price = price * (1 - discount / 100)
    return f_price



def get_product_data(id):
    """return Product(*data)"""
    cursor.execute("""
        SELECT * FROM products WHERE id = ?
    """, (id,))

    data = cursor.fetchone()

    if not data:
        return None

    return Product(*data)


def get_all_products():
    cursor.execute("""
        SELECT * FROM products
    """)

    data = cursor.fetchall()

    return [Product(*product) for product in data]


def edit_product(id, name, price, amount):
    if cursor.execute("""
        UPDATE products
        SET name = ?, price = ?, amount = ?
        WHERE id = ?
    """, (name, price, amount, id)):
        connection.commit()
        return True
    else:
        return False


def order_by(column="id", direction="ASC"):
    allowed_columns = ["id", "name", "price", "amount"]
    allowed_directions = ["ASC", "DESC"]

    if column not in allowed_columns:
        return []

    if direction not in allowed_directions:
        return []

    cursor.execute(f"""
        SELECT * FROM products
        ORDER BY {column} {direction}
    """)

    data = cursor.fetchall()

    return [Product(*product) for product in data]


def search_product(name):
    cursor.execute("""
        SELECT * FROM products
        WHERE name LIKE ?
    """, (f"%{name}%",))

    data = cursor.fetchall()

    return [Product(*product) for product in data]