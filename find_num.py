import random as r


# Computer thought you find

game = "Would you like to play[y/n]>> "

while True:
    a = 0
    n = 0
    input_game = input(game)
    if input_game == 'y':
        computer_num = r.randint(1,10)
        user_input = "Input number>>  "

        while computer_num != user_input:
            number = int(input(user_input))
            a+=1
            if number > computer_num:
                print("it's lower")
                continue
            elif number < computer_num:
                print("It's greater")
                continue
            else:
                print(f"You got it in {a} times")
                break


# you think computer finds
        print("Think of a number I'll try to find")
        computer_predict = r.randint(1, 10)
        ask = f"You thought of a number {computer_predict}"
        ask += "\nIf it's greater, write 'g', if it's lower, write 'l'. If I find it, write 'y'"

        while True:
            ask_num = input(ask)
            n += 1
            if ask_num == "l":
                computer_predict -= 1
            elif ask_num == 'g':
                computer_predict += 1  # Increase by 1 if the guess is too low
            elif ask_num == 'y':
                print(f"I got it within {n} attempts")
                break
            else:
                print("Invalid input. Please enter 'g', 'l', or 'y'.")
                n-=1
                continue
    
            ask = f"Is your number {computer_predict}? ('g', 'l', or 'y')"  # Update the prompt to reflect the new guess

    else:
        print("Good bye!")
        break

    if a < n:
        print(f"You won, i got within {n} attempts but you got within {a} attempts") 
    elif a > n:
        print(f"I won, i got within {n} attempts but you got within {a} attempts")
    else:
        print("It's draw!")