
""" 
write a program that has a user guess a secret number between 1 and 10. 
Store the  secret number in variable called secretNumber
and allow the user to continually input number until they correctly guess what  secretNumber is.
if secretNumber was 6
"""

guessNumber = int(input("Enter your number : "))
secretNumber = 7
while(True):
    if (guessNumber == secretNumber):
        print("Congratulations! You guessed the correct")
        break
    else:
        print("Try again !")
        guessNumber = int(input("Enter your number : "))
