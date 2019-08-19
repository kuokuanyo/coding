#pip install Pillow
from PIL import Image
import os

image_file = Image.open('newcar_2961.jpg.')
image_file = image_file.convert('L')
image_file.save('result.png')

#os.listdir()將資料夾所有資料印出
for file in os.listdir('.'):
	if file.endswith('.jpg'):   #endswith()結尾
		print(file)

#執行多個檔案的jpg
for file in os.listdir('.'):
	if file.endswith('.jpg'):   #endswith()結尾
		image_file = Image.open(file)
		image_file = image_file.convert('L')
		image_file.save(file[:-4]+'_grey.png')   #file[:-4]去掉.jpg

#分開資料夾整理
#原使檔資料夾:original
#執行後:result
for file in os.listdir('original'):
	if file.endswith('.jpg'):   #endswith()結尾
		image_file = Image.open('original/' + file)
		image_file = image_file.convert('L')
		image_file.save('result/' + file[:-4]+'_grey.png')   #file[:-4]去掉.jpg

#os裡有自動路徑合併方法
#os.path.join( , , , )
for file in os.listdir('original'):
	if file.endswith('.jpg'):   #endswith()結尾
		image_file = Image.open(os.path.join('original', file))
		image_file = image_file.convert('L')
		image_file.save(os.path.join('result', file[:-4] + '_grey.png'))   #file[:-4]去掉.jpg
