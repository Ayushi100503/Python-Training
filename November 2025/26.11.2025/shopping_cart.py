class shoppingcart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))
        return(name,"Item added to the shopping cart")

    def remove_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                print(name, " removed from the shopping cart")
                return
            print("Item not in the shopping cart")

    def total_cost(self):
        total_cost = 0
        for item in self.items:
            total_cost += item[1]
        return total_cost

    def apply_discount(self, percent):
        total_cost = self.total_cost()
        discount_amount = total_cost * (percent/100)
        final_price = total_cost - discount_amount
        return final_price

    def display_items(self):
        if not self.items:
            print("cart is empty")
            return
        print("items in the shopping cart:")
        for name, price in self.items:
            print(name, " - ", price)

cart = shoppingcart()

cart.add_item("laptop", 90000)
cart.add_item("milk", 74)
cart.add_item("coffee", 575)
print()
cart.display_items()
print()
print("total cost: ", cart.total_cost())
print("final price: ", cart.apply_discount(10))
print()
cart.remove_item("milk")
cart.display_items()






