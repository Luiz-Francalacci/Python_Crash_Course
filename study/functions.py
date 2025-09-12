"""
def display_message():
    print("Hello, I am learning Python")
display_message()

def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Captain underpants")

def make_tshirt(size = "L", text = "I Love Python"):
    print(f"Tshirt: {text} Size: {size}")

make_tshirt()

make_tshirt("S", "Cool Aid")

make_tshirt(text = "Aid Cool", size = "L")

def describe_city(name, country = "Brazil"):
    print(f"{name.title()} is in {country.title()}")

describe_city("Rio de Janeiro")
describe_city("Nova York")
describe_city("Curitiba")

"""

"""
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

c1 = city_country("Reykjavik", "Iceland")
print(c1)
c2 = city_country("Curitiba", "Brazil")
print(c2)
c3 = city_country("Tokyo", "Japan")
print(c3)


def make_album(artist, album, songs= None):
    if songs is None:
        album = {"arists_name": artist, "album_title": album}
    else:
        album = {"arists_name": artist,"album_title": album, "songs": songs}
    return album

a1 = make_album("Jorge", "Balada")
a2 = make_album("Rita", "Balada", 10)
print(a1)
print(a2)

flag = "a"

while flag != "q":
    opt = input("Digite artista, titulo do album e se quiser musicas. Aperte q para sair")
    if opt == "q":
        flag = "q"
        break
    album_list = opt.split(", ")
    if len(album_list) < 3:
        print(make_album(album_list[0], album_list[1]))
    else:
        print(make_album(album_list[0], album_list[1], album_list[2]))

"""
"""
messages = ["Python is nice","I enjoy fishing","I love burguers"]
def show_messages(msg):
    for x in msg:
        print(x)
show_messages(messages)
sent_messages = []

def send_messages(msg, sent_msg):
    for x in msg[:]:
        print(x)
        sent_msg.append(x)
        msg.remove(x)
send_messages(messages, sent_messages)

print(sent_messages)
print(messages)
"""

def sandwiches(*ingredients):
    print("Sandwich with:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

sandwiches("Cream", "Cookies")
sandwiches("Cheese", "Ham", "Eggs", "Bacon")
sandwiches("Tomato")

def make_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car = make_car("Mercedes", "SL 63", color="Blue", twowd = True)

print(car)