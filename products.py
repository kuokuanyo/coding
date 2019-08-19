#記帳程式
#處理編碼問題
#讀取檔案
import os   #檢查檔案

def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
		#不把商品價格加入list裡
			if '商品,價格' in line:
				continue
			#清除換行符號，以逗點切割
			name, price = line.strip().split(',')   #list
			products.append([name, price])
	return products

def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')

		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		p = []
		p.append(name)
		p.append(price)
		#將產品加入清單
		products.append(p)
	return products

def print_products(products):
	for p in products:
		print(p[0], '價格是', p[1])

def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()