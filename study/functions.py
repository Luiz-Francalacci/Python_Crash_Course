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
