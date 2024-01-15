# sum of the current number and the previous


previous_num = 0
for i in range(1, 11):
    sum = previous_num + i
    print(sum)
    previous_num = i