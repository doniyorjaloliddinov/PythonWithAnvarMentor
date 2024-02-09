# def get_info(name,s_name,b_year,b_place,email="",tel=None):

#     user_info = {
#             "name" : name,
#             "second-name" : s_name, 
#             "b_year" : b_year,
#             "b_place" : b_place,
#             "email" : email,
#             "tel" : tel
#         }
#     return user_info

# # doni = get_info("doni", "sammy", 4555, "usa", "sam@gmail.com", 898998989)
# # print(doni)


# users_info = []
# while True:
#     question = input("Would you like to play[y/n]>> ")
#     if question !='n':
#         name = input("Write your name>> ")
#         s_name = input("Write your second name>> ")
#         b_year = input("Write your bith year>> ")
#         b_place = input("Write your birth place>> ")
#         email = input("write your email adress>> ")
#         tel = input("Write your telephone number(+9989)")
#         users_info.append(get_info(name,s_name,b_year,b_place,email,tel))
#     else:
#         print("Program ended!")
#         break

# for i in users_info:
#     print(f"{i['name'].title()} {i['second-name'].title()} was born in {i['b_year']}.\
#               In {i['b_place']}, his number: {i['tel']} and email adress: {i['email']}")
# print(users_info)


# def maximum(num1,num2,num3):
#     # diff_two_nums = max(num1,num2)
#     # if diff_two_nums > num3:
#     #     return  f"{diff_two_nums} is the maximum"
#     # else:
#     #     return f"{num3} is the maximum"
#     if num1 >= num2 and num1 >= num3:
#         return f"{num1} is the maximum"
#     elif num2 >= num1 and num2 >= num3:
#         return f"{num2} is the maximum"
#     else:
#         return f"{num3} is the maximum"

# max_val = maximum(1223,1223,728)
# print(max_val)


# def prime_numbers(num1,num2):
#     numbers = []
#     for i in range(num1,num2):
#         if i%1==i and i%i==i:
#             numbers.append(i)
#         else:
#             continue
#     print(numbers)
# prime = prime_numbers(10,1000)
# print(prime)

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar


# print(fibonacci(10))