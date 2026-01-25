import os

class Product:

    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount

    def get_value(self):
        return self.price * self.quantity
    
    def is_low_stock(self, threshold=5):
        return self.quantity <= threshold

    def to_csv(self):
        return f"{self.product_id},{self.name},{self.category},{self.price},{self.quantity}"
    
    def __str__(self):
        return (
            f"ID: {self.product_id} | "
            f"{self.name} ({self.category}) | "
            f"Price: {self.price} | "
            f"Qty: {self.quantity}"
        )
        
class Inventory:

    def __init__(self):
        self.products = []
        self.load_from_csv()

    def add_product(self, product):
        for p in self.products:
            if p.product_id == product.product_id:
                print("Product ID already exists.")
                return
        self.products.append(product)
        print(f"Product {product.name} added successfully!")

    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print("Product removed successfully.")
                return
        print("Product not found.")

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                print("Product found successfully.")
                return product
        return None
    
    def display_product(self):
        if not self.products:
            print("Inventory is empty.")
            return
        else:
            print("\n--- Inventory List ---")
            for product in self.products:
                print(product)

    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.get_value()
        return total
    
    def low_stock_report(self, threshold=5):
        print("\n--- Low Stock Products ---")
        found = False
        for product in self.products:
            if product.is_low_stock(threshold):
                print(product)
                found = True
        
        if not found:
            print("No low stock products.")

    def save_to_csv(self):
        with open("inventory.csv", "w") as file:
            file.write("product_id,name,category,price,quantity\n")
            for product in self.products:
                file.write(product.to_csv() + "\n")

    def load_from_csv(self):
        if not os.path.exists("inventory.csv"):
            return
        with open("inventory.csv", "r") as file:
            next(file)
            for line in file:
                pid, name, cat, price, qty = line.strip().split(",")
                product = Product(
                    int(pid),
                    name,
                    cat,
                    float(price),
                    int(qty)
                )
                self.products.append(product)
    
def menu():
    inventory = Inventory()

    while True:
        print("\n===== Inventory Menu =====")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Search Product")
        print("4. Display Product")
        print("5. Total Inventory Value")
        print("6. Low Stock Report")
        print("7. Save & Exit")
       
        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid input. Enter a number between 1-6.")
            continue

        if choice == 1:
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            product = Product(product_id, name, category, price, quantity)

            inventory.add_product(product)

        elif choice == 2:
            pid = int(input("Enter Product ID to Remove: "))
            inventory.remove_product(pid)

        elif choice == 3:
            pid = int(input("Enter Product ID to Search: "))
            product = inventory.search_product(pid)
            if product:
                print(product)
            else:
                print("Product not found.")

        elif choice == 4:
            inventory.display_product()

        elif choice == 5:
            print("Total Inventory Value:", inventory.total_inventory_value())

        elif choice == 6:
            inventory.low_stock_report()

        elif choice == 7:
            inventory.save_to_csv()
            print("Data Saved. GoodBye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()