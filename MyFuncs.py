user_logins = ["admin", "login", "passwd", "qwerty", 12345]

def have_account(usr_option):
#       ===== Have an Account Question mark if-else block  =====
    if usr_option.lower() == 'y':
        usr_login = input("Write down your login>> ")
    elif usr_option.lower() == "n":
        print("Would you like to create an account?[y/n]" )
    else:
        return("Wrong option is given, please restart programm and type y/n")
        
#   ==== Account creation if-else block  ===== 
    if usr_login not in user_logins:
            play = input("Would you like to play?[y/n]")
    else:
        user_logins.append(usr_login)
        print("Account created succesfully")
        play = input("Would you like to play?[y/n]")

#       ===== Would Play Question mark if-else block  =====
    if play.lower() == "y":
         first_num = input("Birinchi raqamni kiriting>> ")
         second_num = input("Ikkinchi raqamni kiriting>> ")
         math_option = input("Matematik amaliyotni tanlang [+ - / * ]")

    elif play.lower() == "n":
         return "Good Bye, See you soon :D"
    
    else:
         return "Good Bye, See you soon :D"
    
#    ========   Math if-else Block ======== 
    if math_option == "+":
            return f"{first_num + second_num}"
    elif math_option == "-":
         return f"{first_num - second_num}"
    elif math_option == "/":
         return f"{second_num / first_num}"
    elif math_option == "*":
         return f"{first_num * second_num}"
    else:
        return "No option available, please run programm again"