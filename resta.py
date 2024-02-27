class RestaurantTable:

    menus = {
        "pizza" : 5000,
        "cola" : 2000,
        "hamburger" :5000,
        "coffee" : 1500,
        "fries" : 3000
    }

    def __init__(self):
        self.orders= []
        self.total = 0
    
    def add_order(self,order):
        self.orders.append(order)
        self.total+=self.menus[order]
    
    def print_bill(self):
        for order in self.orders:
            print(f"{order} : {self.menus[order]}")

        print(f"The total is {self.total}.")

def start_program():
    table = RestaurantTable()
    
    while True:
        order = input("Order[pizza,cola,fries,hamburger,coffee]: ")
        table.add_order(order)

        another = input("Order again? y/n : ")
        if another == "y":
            continue
        elif another == "n":
            table.print_bill()
            break

start_program()