import pickle
file_name  = "pi_million_digits.txt"

# # file_name = "salom.txt"

# # with open(file_name, "r") as file:
# #     f = file.read()

# # print(f)


with open(file_name, "r") as file:
    PI = (str(file.read()))
    PI = PI.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
    PI = PI.replace('\n','') # qator tashlash belgisini almashtiramiz
# print(PI)

# def is_birhtday_contains_in_pi(b_date:int):
#     """Write your birth date in this order: D:M:Y Ex: 9012003"""
#     pi = float(PI)
#     if b_date in pi:
#         print(f"{b_date} is here")
#     else:
#         print(f"{b_date} is not found!")
# is_birhtday_contains_in_pi(9012003)

print("55555" in PI)

with open("pi_float.dat", 'wb') as file:
    pickle.dump(PI,file)