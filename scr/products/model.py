class Product:
    def __init__(self, id, name, price, amount):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount

    def get_total(self):
        return self.price * self.amount