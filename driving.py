country = input('請問你是哪國人: ') #str
age = input('請輸入年齡: ') #str
age = int(age) #int

if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不能考駕照')

elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你不能考駕照')

else:
	print('你只能輸入台灣與美國')