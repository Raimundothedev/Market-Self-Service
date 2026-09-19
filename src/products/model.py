from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    amount: int

    def get_total(self):
        return self.price * self.amount