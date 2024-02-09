# user_meal = ("What would you like to eat (to stop, write: stop)>> ")
# meals = []

# grocery = {
#     "meat" : 4555,
#     "bread" : 1500,
#     "apple" : 7800,
#     "banana" : 35000,
#     "salad" : 25000,
#     "tea" : 65000,
#     "sugar" : 15000
# }

# while True:
#     meal = input(user_meal)
#     if meal == "stop":
#         break
#     else:
#         meals.append(meal)
    
# # print("Currently we have: ")
# while meals:
#     order = meals.pop()
#     if order in grocery.keys():
#         print(f"{order} is {grocery[order]}")
#     else:
#         print(f"Sorry, but we dont't have: {order}")

# print("E-commerce")

# store = {}
# user_meal = "Write what you would like to add"
# user_meal += "(In order to stop programm, write: stop)>> "

# while True:
#     meal = input(user_meal)
#     if meal != "stop":
#         price = int(input(f"Write {meal}'s price>> "))
#         store[meal] = price
#     else:
#         break

# print("All added: ")
# for k,v in store.items():
#     print(f"{k} is {v} sum")
# print(store)