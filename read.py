#空list
data = []
count = 0

#讀取檔案
with open('/users/user/desktop/reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		#print(len(data)) print在cmd上面很花時間
		if count % 1000 == 0: # %求餘數
			print(len(data))

print('總共有', len(data), '筆資料')

#算留言平均長度
sum_len = 0

for d in data:
	l = len(d)
	sum_len += l

final_mean = sum_len / len(data)

print('每筆留言的平均長度: ', final_mean)

new = []
for d in data:
	if len(d) < 100:   #留言長度小於100
		new.append(d)

print('一共有', len(new), '筆留言長度小於100')

#快寫法(串列生成式)
#當需要使用迴圈，並有條件時，可以使用串列生成式
good = [d for d in data if 'good' in d]
print(len(good))

#原始寫法
for d in data:
	bad.append('bad' in d)

bad = ['bad' in d for d in data] #印出一堆True or False
print(bad)