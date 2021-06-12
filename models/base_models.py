
class User:
    def __init__(self):
        self.username = None
        self.wallet_amount = None

    def add_user(self, username, wallet_amont):
        self.username = username
        self.wallet_amount = wallet_amont


class Item:
    def __init__(self):
        self.category = None
        self.brand = None
        self.price = None

    def create_item(self, category, brand, price):
        self.category = category
        self.brand = brand
        self.price = price


class Inventory:
    def __init__(self):
        self.items = []
        self.quantity = []

    def add_inventory(self, item, quantity):
        self.items.append(item)
        self.quantity.append(quantity)
        print("Item added to inventory successfully")

    def get_inventory(self):
        inventory = {}
        for item in self.items:
            position = self.items.index(item)
            inventory[(item.category, item.brand)] = self.quantity[position]
        return inventory


class Cart:
    def __init__(self):
        self.user = None
        self.items = []
        self.quantity = []

    def add_to_cart(self, user, item, quantity):
        self.user = user
        self.items.append(item)
        self.quantity.append(quantity)
        print("Item added to cart successfully")

    def update_cart(self, item, quantity):
        position = self.items.index(item)
        self.quantity[position] = quantity
        print("Cart updated successfully")

    def remove_from_cart(self, item):
        position = self.items.index(item)
        try:
            self.items.pop(position)
            self.quantity.pop(position)
            print("Item removed from cart")
        except:
            print("Item not in cart")

    def get_cart(self):
        cart = {}
        for item in self.items:
            position = self.items.index(item)
            cart[(item.category, item.brand)] = self.quantity[position]
        print(cart)
