#一般定義的class開頭都是大寫
class Desk:
    def __init__(self, color):
        self.color = color
        print('我被製造出來了')

    def re_color(self, new_color):
        self.color = new_color

d = Desk('Blue')
print(d.color)
d.re_color('red')
print(d.color)