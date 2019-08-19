#建立一個計數的函示
def count_products(data):
    products = {}
    for p in data:
        product, count = p.split(' ')
        count = int(count)
        if product in products:
            products[product] += count #更改數值
        else:
            products[product] = count #新建字典
    return products

data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
print(count_products(data))