import json
# import json
# # data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# # with open("cars.json", "w") as file:
# #     file.write(str(data))

# # with open("cars.json", "r") as file:
# #     contents = file.read()
# #     print(contents)
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
# dic = json.loads(talaba_json)
# print(f"{dic["ism"]} {dic["familiya"]}")
# # print(type(talaba_json))

# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
# dic = json.loads(talaba_json)
# print(type(dic))
# print(f"{dic["ism"]} {dic["familiya"]}")

# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}""" 
# with open("student.json", "w") as file:
#     data = json.dumps(talaba_json)
#     file.write(data)
# print(type(data))
# print((data))
file_name = "talabalar.json"
with open(file_name) as file:
    data = json.load(file)
for student in data['student']: 
    print(f"{student["name"]} {student["lastname"]}, {student["year"]}, Faculty: {student["faculty"]}")

