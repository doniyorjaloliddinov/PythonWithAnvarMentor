# import random as r
# from uzwords import words

# def get_word():
#     some_word = r.choice(words)
#     while "-" in some_word or " " in some_word:
#        some_word = r.choice(words)
#     return some_word.upper()
    

# def display(user_letters, some_word):
#     display_letter = ""
#     for letter in some_word:
#         if letter in user_letters:
#             display_letter += letter
#         else:
#             display_letter += '-'
#     return display_letter


# def play():
#     word = get_word()
#     word_letters = set(word)
#     user_letters = ""
#     print(f"I have thought word thats length {len(word)} letters.Can you guess?")
#     while len(word_letters)>0:
#         print(display(user_letters, word))
#         if len(user_letters)>0:
#             print(f"Letters that you have written {user_letters}")
        
#         letter = input("Write letter>> ").upper()
#         if letter in user_letters:
#             print("The letter exist already!")
#         elif letter in word:
#             word_letters.remove(letter)
#             print("Correct letter")
#         else:
#             print("Incorrect input")
#             continue

#         user_letters+= letter
#     print(f"Congrats! You found word within {len(user_letters)} times")

import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)    
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    # print(word)
    while word_letters:
        print(display(user_letters,word))
        if user_letters:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")
        
        letter = input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
            continue        
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")