def max_num(num1,num2,num3):
    max_of_two = max(num1,num2)
    if num3 > max_of_two:
        return num3
    elif num3 < max_of_two:
        return max_of_two
    else:
        return F"Two or three numbers are equal!"
# print(max_num(45,55,-5))
# print(max_num(45,55,55))
# print(max_num(45,55,54))
# print(max_num(5,55,-5))
# print(max_num(45,5.5,-5))

hello = ["hello world, my name is doni", "hi jimmy", "bye sonny"]
def capitalizer(texts):
    for text in texts:
        print(text.replace(text[0], text[0].capitalize()))

# print(capitalizer(hello))
        
def even_nums(*nums):
    even = []
    for num in nums:
        if num%2==0:
            even.append(num)
        else:
            continue
    return even
# print(even_nums(1,2,3,4,5,6,7,8,9))

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while a < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(100))