from database.database import cursor, connection
from products.model import Product
from currency import converter
from config import config


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

def convert_all_prices(to_currency):
    from_currency = config.load_config().get("currency")
    products = get_all_products()

    for product in products:
        price = converter.from_usd(
            converter.to_usd(parse_price(product.price), from_currency),
            to_currency
        )

        edit_product(
            product.id,
            product.name,
            price,
            product.amount
        )
    return True

def parse_price(value):
    if isinstance(value, float):
        return value
    value = value.strip()

    if "," in value:
        value = value.replace(".", "")
        value = value.replace(",", ".")

    elif "." in value:
        parts = value.split(".")

        if len(parts[-1]) == 3:
            value = value.replace(".", "")

    return float(value)
    



def order_by(column="id", direction="DESC"):
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