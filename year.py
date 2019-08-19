#判斷是不是閏年
def is_leap(year):
	if year % 4 != 0:
		print('平年')
		return False
	elif year % 4 == 0 and year % 100 != 0:
		print('閏年')
		return True
	elif year % 100 == 0 and year % 400 != 0:
		print('平年')
		return False
	elif year % 400 == 0 and year % 3200 != 0:
		print('閏年') 
		return True

#第一種清單加法
def sum_of_list(numbers):
	return sum(numbers)

print(sum_of_list([1,2,3]))

#第二種
def sum_of_list_2(numbers):
	sum_number = 0
	for number in numbers:
		sum_number += number
	return sum_number