# Python program to display all the prime numbers within an interval

lower = int(input("Enter your lower number : "))
upper = int(input("Enter your lower number : "))

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)