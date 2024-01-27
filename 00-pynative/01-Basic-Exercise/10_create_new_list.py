



def merge_list(list1, list2):
    result_list = []
    
    for i in list1:
        if i % 2 != 0:
            result_list.append(i)
    
    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
    return result_list


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result = merge_list(list1, list2)
print(result)