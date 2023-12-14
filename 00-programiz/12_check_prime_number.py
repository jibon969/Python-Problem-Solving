# Check Prime Number
""" 
A prime number can be defined as a natural number greater than 1
whose only factors are 1 and the number itself. 
"""

is_prime = int(input("Enter your number : "))
for i in range(2, is_prime):
    if is_prime % i == 0:
        print("Not a prime number ")
        break
else:
    print("Its Prime")
