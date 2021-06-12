class CartCheckoutService:
    def checkout_cart(self, inventory, cart):

        all_items = inventory.items
        total_quantity = inventory.quantity

        # Inventory check
        for item in cart.items:
            if item not in all_items:
                print("{}: {} not available".format(
                    item.category, item. brand))
                break
            inventory_position = all_items.index(item)
            cart_position = cart.items.index(item)
            if cart.quantity[cart_position] > total_quantity[inventory_position]:
                print("Quantity not available")
                break

        # Wallet balance check
        amount = 0

        for item in cart.items:
            inventory_position = all_items.index(item)
            cart_position = cart.items.index(item)
            amount += item.price * cart.quantity[cart_position]
            total_quantity[inventory_position] -= cart.quantity[cart_position]

        if cart.user.wallet_amount < amount:
            print("Insufficient balance")
