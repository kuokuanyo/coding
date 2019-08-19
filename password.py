#建立密碼重試程式
#password = a123456
#最多輸入三次

i = 3 #次數
password = 'a123456'

#建立密碼迴圈
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼: ')

	if pwd == password:
		print('登入成功!')
		break

	else:
		print('密碼錯誤!') 
		if i > 0:
			print('還有i次機會')
		else:
			print('沒機會嘗試了')
		
		