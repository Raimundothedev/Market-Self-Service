from products.repository import *


product = get_product_data(2)

if product:
    print(product.name)
    print(product.price)
    print(product.amount)
    print(product.get_total())