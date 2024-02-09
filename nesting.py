# messi = {
#     "name" : "Messi",
#     "club" : "Barcelona",
#     "age" : 35,
#     "b_place" : "Argentina"
# }

# ronaldo = {
#     "name" : "Ronaldo",
#     "club" : "Real Madrid",
#     "age" : 38,
#     "b_place" : "Portugal"
# }

# neymar = {
#     "name" : "Neymar",
#     "club" : "Brazil", 
#     "age" : 32,
#     "b_place" : "Brazil"
# }

# suarez = {
#     "name" : "Suarez",
#      "club" : "Barcelona",
#      "age" : 33, 
#      "b_place" : "Urugvay"
# }

# fooballers = [suarez, ronaldo, messi, neymar]

# for fooball in fooballers:
#     name = fooball["name"]
#     club = fooball["club"]
#     age = fooball["age"]
#     b_place = fooball["b_place"]

#     print(f"{name} was born in {b_place}. "
#           f"Plays in {club} and he comes from  {b_place}")


# soap_opera = {
#     "Sammy" : ["Pokemon", "Mango", "Sardini", "Lian"],
#     "Lammy" : ["Sherman", "Mango", "Tanks", "harry potter"],
#     "Robert" : ["War and peace", "Mango", "Sardini", "harry potter"],
#     "John" : ["Son", "Lord", "Sardini", "harry potter"]
# }

# for k,v in soap_opera.items():
#     print(f"\n{k}'s lovely movies are:")
#     for movie in v:
#         print(f"{movie}")

countries  = {
    "usa" : { 
        "population" : 30000000,
        "currency" : "usd",
        "capital" : "Washington D.C"
    },
    "uzbekistan" :
        {
            "population" : 400000,
            "currency" : "uzs",
            "capital" : "tashkent"
        },
    "kazakhstan" :
        {
            "population" : 5600000,
            "currency" : "tenge",
            "capital" : "astana"
        },
    "uae" : {
        "population" : 1800000,
        "currency" : "dirham",
        "capital" : "Abu Dhabi"
    }
}

usr_req = input("Wich country info would you like to know>> ").lower()
if usr_req in countries:
    info = countries[usr_req]
    print(f"{usr_req.upper()}'s capital is {info['capital']}"
          f"And its population: {info['population']}, currency {info['currency']}")
else:
    print("No such country on my list")