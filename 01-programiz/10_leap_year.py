# Python Program to Check Leap Year

""" 
A leap year is a calendar year that has an extra day, or month, compared to a common year
Any year that is evenly divisible by 4 is a leap year: for example, 1988, 1992, and 1996 are leap years
"""

# import calendar
# year = int(input("Enter your year : "))
# month = int(input("Enter your year : "))
# output = calendar.month(year, month)
# print(output)

# year = calendar.calendar(2024)
# print(year)


year = int(input("Enter your your : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("leap Year")
else:
    print("Not leap year ")
    
    
