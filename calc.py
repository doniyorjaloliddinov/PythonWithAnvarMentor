passwd = ["login", "admin", "qwerty", 12345, "doni"]
usr_acc = input("Do you have account [y/n]>> ")


if usr_acc.lower() == "y":
    login = input("Write your login>> ")
    if login in passwd:
        print("You are loged up!")
    else:
        print("No such kind of account exist, please try again!")
    
        while True:
            if login not in passwd:
                creat_acc = input("Write new account>> ")
                passwd.append(creat_acc)
                break

print(passwd)

would_play = ("Do you want to play [y/n]>> ")

while would_play != "exit":
    play = input(would_play)
    if play.lower() == "y":
        first_num = float(input("Write first number>> "))
        math = input("Please choose option [/ * - + ]>> ")
        second_num = float(input("Write second number>> "))
        if math == "/":
            print(f"{first_num / second_num}")
        if math == "*":
            print(f"{first_num * second_num}")
        if math == "-":
            print(f"{first_num - second_num}")   
        if math == "+":
            print(f"{first_num + second_num}")
    else:
        print("Exited!")
        break