class RestaurantTable :

    menu = {
        "pizza" : 3000,
        "apple juice" : 2000,
        "hamburger" : 4000,
        "coffee" : 1500,
        "french fires" : 2500,
    }

    def __init__(self) :
        self.total = 0
        self.orders = []

    def add_order(self,order) :
        self.orders.append(order)
        self.total += self.menu[order]

    def bill(self) :
        for order in self.orders:
            print(f"{order} : {self.menu[order]}")

        print(f"Total is {self.total}")

    
def start_order() :
    table = RestaurantTable()

    while True:
        order = input("Order : ")
        table.add_order(order)

        another = input("Again ?? y /n : ")
        if (another == "y") :
            continue
        else : 
            table.bill()
            break

start_order()

    