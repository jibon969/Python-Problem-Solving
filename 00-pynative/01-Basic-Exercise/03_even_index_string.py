# Print characters from a string that are present at an even index number

my_name = input("Enter your name : ")
name = list(my_name)
for i in name:
    print(i[::2])