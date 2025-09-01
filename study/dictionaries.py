person = {'first_name' : 'Luiz', 'last_name' : 'Francalacci'
    , 'age': 22, 'city' : 'Tokyo'}

print(f"{person['first_name']} {person['last_name']} {person['age']} {person['city']}")

for key, value in person.items():
    print(f"{key} = {value}")

favorite_lang ={'Jorge': 'Python', 'Manoel': 'Java', 'Larissa': 'Ruby', 'Camilla': 'C#'}

for k,v in favorite_lang.items():
    print(f"{k}'s favorite language is {v}")

for k in favorite_lang.keys():
    print(f"{k}")

for v in favorite_lang.values():
    print(f"{v}")

cities = {'São Paulo': {'Population': 10000, 'State': 'São Paulo'},
          'Curitiba': {'Population': 1022003310, 'State': 'Parana'},
          'Fortaleza': {'Population': 1341210, 'State': 'Ceara'}}

for k,v in cities.items():
    print(f"{k}: ")
    for k2, v2 in v.items():
        print(f"{k2} = {v2}")
    print("\n")