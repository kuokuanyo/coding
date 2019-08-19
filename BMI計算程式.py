height = input('請輸入身高(cm): ')
weight = input('請輸入體重(kg) : ')

height = int(height) / 100
weight = int(weight)

bmi = weight / height / height

if bim < 18.5:
	print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('體重正常')
elif bmi >= 24 and bmi < 27:
	print('過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
elif bmi >= 35:
	print('重度肥胖')