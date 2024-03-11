"""
Given two numbers num1 and num2. 
The task is to write a Python program to find the addition of these two numbers. 
"""

"""
Using “+” operator
Defining a function that adds two number
Using operator.add method
Using lambda function
Using Recursive function
"""

# Example of => + operator
num1 = 5
num2 = 2

sum = num1 + num2
print(sum)


# Defining a function that adds two number
def add_two_number(x, y):
    return x + y

result = add_two_number(5, 2)
print("Result : ", result)


# Using lambda function
result = lambda a, b : a + b
x = result(5, 2)
print("lambda : ", x)