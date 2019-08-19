#多行式註解快捷鍵: ctrl+/
#文字計數(字典)
import time

data = []
count = 0
wc = {}   #word_count

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

start_time = time.time()

for d in data:
	words = d.split(' ')   #list
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1   #increse key
		
while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過~')

end_time = time.time()
print(end_time + start_time, 'seconds')