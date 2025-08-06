class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def product_catalogue(self):
        # Display the product's information
        print(f"Product Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def total_value(self):
        # Calculate and return total value
        return self.price * self.quantity
# Create an instance (object) of product 
product1 = product("Laptop", 999.99, 5)

product1.product_catalogue()
print(f"Total value in stock: ${product1.total_value()}")