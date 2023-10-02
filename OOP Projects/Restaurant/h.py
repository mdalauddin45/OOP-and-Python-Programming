class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description} - ${self.price:.2f}"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def display_menu(self):
        print("Menu:")
        for item in self.items:
            print(item)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        self.items.extend([item] * quantity)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

    def display_order(self):
        print("Order:")
        for item in self.items:
            print(item)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.orders = []

    def create_menu(self):
        item1 = MenuItem("Burger", "Delicious burger with cheese", 5.99)
        item2 = MenuItem("Pizza", "Margherita pizza with tomato and mozzarella", 8.99)
        item3 = MenuItem("Pasta", "Spaghetti with marinara sauce", 7.49)
        
        self.menu.add_item(item1)
        self.menu.add_item(item2)
        self.menu.add_item(item3)

    def take_order(self, order):
        self.orders.append(order)

    def display_orders(self):
        for index, order in enumerate(self.orders, start=1):
            print(f"Order {index}:")
            order.display_order()
            total = order.calculate_total()
            print(f"Total: ${total:.2f}\n")

if __name__ == "__main__":
    restaurant = Restaurant("Sample Restaurant")
    restaurant.create_menu()

    while True:
        print("\nOptions:")
        print("1. Display Menu")
        print("2. Place Order")
        print("3. Display Orders")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            restaurant.menu.display_menu()
        elif choice == "2":
            order = Order()
            while True:
                item_name = input("Enter item name to order (or 'done' to finish): ")
                if item_name.lower() == "done":
                    break
                item = next((menu_item for menu_item in restaurant.menu.items if menu_item.name == item_name), None)
                if item:
                    quantity = int(input(f"Enter quantity for '{item_name}': "))
                    order.add_item(item, quantity)
                else:
                    print(f"'{item_name}' not found in the menu.")
            restaurant.take_order(order)
        elif choice == "3":
            restaurant.display_orders()
        elif choice == "4":
            print("Exiting the restaurant management system.")
            break
        else:
            print("Invalid choice. Please try again.")
