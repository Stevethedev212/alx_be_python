class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        return self.price * self.quantity
# Example usage

item1 = Item("phone", 100, 5)
item2 = Item("laptop", 1000, 3)

