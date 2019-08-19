#產生隨機整數1~100

import random

s = input('請決定隨機數字初始值: ')
e = input('請決定隨機數字結束值: ')
s = int(s)
e = int(e)

r = random.randint(s,e)
i = 0  #猜的次數

while  True:
	num = input('請輸入數字: ')
	num = int(num)
	i += 1

	if num == r:
		print('終於猜對了!')
		print('總共猜了', i, '次')
		break
	elif num < r:
		print('比答案小')
	else:
		print('比答案大')
	print('猜了第', i, '次')
	