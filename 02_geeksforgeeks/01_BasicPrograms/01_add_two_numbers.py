
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


# operator.add method
import operator
x = 5
y = 6
z = operator.add(x, y)
print("operator.add method :", z)


# Define a recursive function to add two numbers
def add_numbers_recursive(x, y):
	if y == 0:
		return x
	else:
		return add_numbers_recursive(x + 1, y - 1)

# Take input from the user
num1 = 32
num2 = 2

# Call the recursive function to add the two numbers
result = add_numbers_recursive(num1, num2)

# Print the result
print("The sum of", num1, "and", num2, "is", result)
