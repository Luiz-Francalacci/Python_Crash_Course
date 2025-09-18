from study.POO.classes import Restaurant
from study.POO.classes import User

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


class Admin(User):
    def __init__(self, first_name, last_name, age, email, cpf):
        super().__init__(first_name, last_name, age, email, cpf)
        self.privileges = ["Can add post", "Can remove post", "Can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"{privilege}")

adm = Admin("Luiz", "Francalacci", 22, "1551@gmail.com", "123456789")
adm.greet_user()
adm.describe_user()
adm.show_privileges()

