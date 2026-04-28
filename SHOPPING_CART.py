# Create ta diri og class para sa atong Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.cart = []

    # View items in cart
    def view_cart(self):
        if len(self.cart) == 0:
            print("\nYour cart is empty.")
        else:
            print("\nItems in your cart:")
            for i in range(len(self.cart)):
                print(f"{i+1}. {self.cart[i]}")

    # Add item sa cart
    def add_item(self):
        item = input("\nEnter item to add: ")
        self.cart.append(item)
        print(item, "added to cart.")

    # Remove item sa cart
    def remove_item(self):
        if len(self.cart) == 0:
            print("\nCart is empty.")
        else:
            self.view_cart()
            index = int(input("\nEnter item number to remove: ")) - 1

            if 0 <= index < len(self.cart):
                removed = self.cart.pop(index)
                print(removed, "removed from cart.")
            else:
                print("Invalid item number.")

    # Checkout
    def checkout(self):
        if len(self.cart) == 0:
            print("\nYour cart is empty.")
        else:
            print("\nChecking out the following items:")
            for item in self.cart:
                print("-", item)
            print("Thank you for shopping!")

            self.cart.clear() # Diri i clear niya ang shopping cart


# Create an object of the class
cart_system = ShoppingCart()

# Menu system
while True:
    print("\nShopping Cart Simulator")
    print("1. View Cart")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Checkout")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        cart_system.view_cart()

    elif choice == "2":
        cart_system.add_item()

    elif choice == "3":
        cart_system.remove_item()

    elif choice == "4":
        cart_system.checkout()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")

        hello
        