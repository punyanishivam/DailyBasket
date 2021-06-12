from models.base_models import User, Item, Inventory, Cart
from services.CartCheckoutService import CartCheckoutService
# Testing functionality


# Add user in the system --> addUser(userName, walletAmout)
user1 = User()
user1.add_user("Amit", 500)
# print(user1)
user2 = User()
user2.add_user("Goku", 1000)
# print(user2)

# Create an item --> createItem(itemCategory, brand, price)
item1 = Item()
item1.create_item("Chocolate", "Cadbury", 50)
# print(item1)
item2 = Item()
item2.create_item("Chocolate", "Parle", 10)
# print(item2)
item3 = Item()
item3.create_item("Butter", "Amul", 10)
# print(item3)
item4 = Item()
item4.create_item("Milk", "Amul", 25)
# print(item4)

# Add item to inventory --> addInventory(itemCategory, brand, quantity)
inventory = Inventory()
inventory.add_inventory(item4, 10)
inventory.add_inventory(item3, 20)
inventory.add_inventory(item1, 20)
inventory.add_inventory(item2, 15)
print(inventory.get_inventory())
# print(inventory)


# Add/remove items to the user’s current cart --> addToCart(userName,
# itemCategory, brand, quantity)
cart = Cart()
cart.add_to_cart(user1, item4, 5)
cart.add_to_cart(user1, item1, 10)
# print(cart.user, cart.items, cart.quantity)
cart.update_cart(item4, 4)
# print(cart.user, cart.items, cart.quantity)
cart.remove_from_cart(item4)
# print(cart.user, cart.items, cart.quantity)


# Get the current cart info of the user --> getCart(userName)
cart.get_cart()

# Cart checkout for a user --> cartCheckout(userName)
cart_checkout_service = CartCheckoutService()
cart_checkout_service.checkout_cart(inventory, cart)
