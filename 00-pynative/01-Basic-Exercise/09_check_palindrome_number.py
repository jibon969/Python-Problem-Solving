# Check Palindrome Number

s = input("Enter the value : ")
reverse = s[::-1]

if (s == reverse):
    print("Yes, it is palindrome number")
else:
    print("No, it is palindrome number")