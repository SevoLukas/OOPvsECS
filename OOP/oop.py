import random
import string

class Product:
    def __init__(self, product_id: int, name: str, description: str, price: int):
        self.id = product_id
        self.name = name
        self.description = description
        self.price = price


def create_products(num_products: int = 1000):
    """
    Creates a list of Product objects with random names, descriptions, and prices.
    """
    products = []
    for i in range(num_products):
        # Generate a random name (length 8 chars)
        name = ''.join(random.choices(string.ascii_letters, k=8))
        # Generate a random description (length 20 chars including spaces)
        description = ''.join(random.choices(string.ascii_letters + ' ', k=20))
        # Generate a random price between 100 and 10,000 (e.g., in cents)
        price = random.randint(100, 10000)
        product = Product(product_id=i, name=name, description=description, price=price)
        products.append(product)

    return products


products = create_products()
for product in products:
    if product.price > 1000:
        product.price = product.price * 0.9