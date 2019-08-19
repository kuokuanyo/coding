#寫出function找出清單中最大的數字
def find_max(a_list):
    if len(a_list) == 0:
        return 0
    else:
        return max(a_list)

print(find_max([1, 2, 3]))
print(find_max([1, -1, -5]))
print(find_max([]))

#解答寫法
def find_max1(a_list):
    if not a_list: #假設a_list是空清單，會回傳FALSE
        return 0 
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

print(find_max1([1, 2, 3]))
print(find_max1([1, -1, -5]))
print(find_max1([]))