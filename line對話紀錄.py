#處理line留言
#讀取檔案
def read_file(filename):
	lines = []
	with open (filename, 'r') as f:
		for line in f:
			lines.append(line.strip())
	return lines
#轉換
#清單切割   n[開始:結束]
def convert(lines):
	new = []
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	for line in lines:
		s = line.split(' ')   #list
		time = s[0]
		name = s[1]
		if name == 'allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m) 
		elif name == 'viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m) 
	print('allen說了', allen_word_count, '個字')
	print('viki說了', viki_word_count, '個字')
	print('allen傳了', allen_sticker_count, '個貼圖')
	print('viki傳了', viki_sticker_count, '個貼圖')

#主要函式
def main():
	lines = read_file('input.txt')
	lines = convert(lines)