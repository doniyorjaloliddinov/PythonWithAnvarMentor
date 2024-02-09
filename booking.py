# hotels = {
#     "Intercontinental" : {
#         "star" : 5,
#         "rooms" : 2,
#         "pool" : True,
#         "price" : 120,
#         "breakfast" : False
#     },
#     "Grand Mir" : {
#         "star" : 3,
#         "rooms" : 5,
#         "pool" : False,
#         "price" : 150,
#         "breakfast" : True
#     },
#     "Poytaxt" : {
#         "star" : 2,
#         "rooms" : 3,
#         "pool" : False,
#         "price" : 50,
#         "breakfast" : False
#     },
#     "Silk Way" : {
#         "star" : 1,
#         "rooms" : 1,
#         "pool" : False,
#         "price" : 43,
#         "breakfast" : True
#     },
#     "Turon" : {
#         "star" : 4,
#         "rooms" : 7,
#         "pool" : True,
#         "price" : 250,
#         "breakfast" : True
#     }
# }
# print("Welcome to Booking.com!")
# user_search = input("Search hotels by [start, pool, price, breakfast, rooms, name]>> ")

# for k,v in hotels.items():
#     if user_search == "name":
#         search_by_name = input("Write hotel name>> ").capitalize()
#         if search_by_name in hotels.keys():
#                 print(f"{search_by_name} is available")
#                 break
#         else:
#              print(f"Sorry, we don't hotel named {search_by_name}")

#     elif user_search == "rooms":
#         search_by_room = int(input("How many rooms do you want: "))
#         available_hotels = [hotel for hotel, details in hotels.items() if details["rooms"] >= search_by_room]

#         if available_hotels:
#             print(f"These hotels have {search_by_room} or more rooms available:")
#             for hotel in available_hotels:
#                 print(hotel)
#                 break
#         else:
#             print("No hotels have the requested number of rooms available.")

    # elif user_search == "breakfast":
    #      pass
    # elif user_search == "pool":
    #      pass
    # elif user_search == "price":
    #      pass
    # elif user_search == "star":
    #      pass



import math_mod as m

m.hello_world()
# print(hello_world())