# 1: Calculate the multiplication and sum of two numbers
""" 
Given two integer numbers, return their product only if the product is equal to or lower than 1000.
Otherwise, return their sum.
"""

num1 = 30
num2 = 50

def multiplication_and_sum(num1, num2):
    if num1 + num2 < 1000:
        sum = num1 + num2
        return sum
    else:
        mul = num1 * num2
        return mul
       

output = multiplication_and_sum(20, 30)
print(output)