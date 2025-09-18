
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}"
              f" and the cuisine type is {self.cuisine_type}")


    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increase_number_served(self, increase):
        self.number_served += increase


r1 = Restaurant("Zucca", "Burguers")
r1.describe_restaurant()
r1.open_restaurant()
print(f"{r1.number_served} clients served")
r1.set_number_served(5)
print(f"{r1.number_served} clients served")
r1.increase_number_served(12)
print(f"{r1.number_served} clients served")




class User:
    def __init__(self, first_name, last_name, age, email, cpf):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.cpf = cpf
        self.login_attempts = 0

    def describe_user(self):
        print(f"""
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Age: {self.age}
        Email: {self.email}
        CPF: {self.cpf}
        """)

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

u1 = User("Marcos", "Karlos", 21, "marquinho@gmail.com", "11243511106")
u1.greet_user()
u1.describe_user()
print(f"Login Attempts: {u1.login_attempts}")
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
print(f"Login Attempts: {u1.login_attempts}")
u1.increment_login_attempts()
u1.increment_login_attempts()
print(f"Login Attempts: {u1.login_attempts}")
u1.reset_login_attempts()
print(f"Login Attempts: {u1.login_attempts}")







