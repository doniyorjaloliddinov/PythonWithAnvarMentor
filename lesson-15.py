# python = {
#     "bool" : "True or false values",
#     "int" : "Interger variable", 
#     "str" : "Letter type variables", 
#     "tuple" : "Set of unrepeatable values", 
#     "list" : "List of values, variable type",
#     "if" : "if condition statement", 
#     "for" : "iteration cycle"
# }

# for k,v in python.items():
#     print(f"{k} is {v}")

# countries = {
#     "uzbekistan" : "Tashkent",
#     "usa" : "Washington",
#     "tajikistan" : "Dushanbe",
#     "italy" : "Rome",
#     "russia" : "Moscow",
#     "malaysia" : "Kuala Lampur",
#     "kazakhstan" : "Nursultan",
#     "afganistan" : "Kabul",
#     "brazil" : "Brazilia",
#     "gb" : "London",
#     "germany" : "Berlin"
# }

# # print("World contries: Their capitals")
# # for k,v in sorted(countries.items()):
# #     print(f"{k} : {v}")
# usr_req = input("Which countries capital would like to know>> ").lower()
# if usr_req in countries.keys():
#     print(f"{usr_req}-ning poytaxti {countries[usr_req]}")
# else:
#     print("No such country on my list(")


# menu = {
#     "plov" : 35000,
#     "manti" : 40000,
#     "salad" : 25000,
#     "bread" : 5000,
#     "lagman" : 35000,
#     "norin" : 40000
# }

# usr_current_meal = []
# print("Order 3 meal")
# for i in range(3):
#     usr_meal = input(f"{i+1} - meal> ")
#     usr_current_meal.append(usr_meal)
# for meal in usr_current_meal: 
#     if meal in menu.keys():
#         print(f"{meal} - {menu[meal]} sum")
#     else:
#         print(f"Sorry, but we don't have {meal}")