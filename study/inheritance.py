from classes import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate", "Strawberry", "Vanilla", "Mint Chocolate"]

    def show_flavors(self):
        print("Ice Cream Flavors: ")
        x = 1
        for flavor in self.flavors:
            print(f"{x}- {flavor}")
            x += 1


ice = IceCreamStand("Vanilla Ice Ice Cream", "Ice Cream")

ice.describe_restaurant()
ice.show_flavors()
ice.increase_number_served(2)
print(ice.number_served)