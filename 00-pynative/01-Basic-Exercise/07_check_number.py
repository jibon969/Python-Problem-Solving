
# Check if the first and last number of a list is the same

# numbers_x = [10, 20, 30, 40, 10]
# x = numbers_x[0]
# y = numbers_x[-1]
# if x == y:
#     print("True")
# else:
#     print("False ")

def number_check(number_list):
    x = number_list[0]
    y = number_list[-1]

    if x == y:
        return True
    else:
        False

numbers_x = [10, 20, 30, 40, 10]
print("result is : ", number_check(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is : ", number_check(numbers_y))

