# How to Add Two Numbers in Python – Easy Programs
""" 
Input: num1 = 5, num2 = 3
Output: 8
Input: num1 = 13, num2 = 6
Output: 19
"""

# num1 = 5
# num2 = 3

# # Adding two number
# sum = num1 + num2
# # printing values
# print("Sum of", num1, "and", num2 , "is", sum)


# Add Two Numbers with User Input ===================================
# number1 = int(input("Enter 1st number : "))
# number2 = int(input("Enter 2nd number : "))
# # Adding two number
# sum = number1 + number2
# # # printing values
# print("Sum of", number1, "and", number2 , "is", sum)


# Add Two Numbers in Python Using Function =========================
# def add_two_number(number1, number2):
#     return number1 + number2

# result = add_two_number(10, 4)
# print(result)


# Add Two Numbers Using operator.add() Method ==========================
# import operator
# num1 = 15
# num2 = 12
# result = operator.add(num1, num2)
# print(result)


# Add Two Number Using Lambda Function ==============================
add_number = lambda x, y : x + y
x =  5
y = 6

result = add_number(x, y)
print(result)
