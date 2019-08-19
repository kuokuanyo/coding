#一般定義的class開頭都是大寫
#class好處
#把相關的function收納在一起
#透過self共用身上的屬性
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


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        print('我誕生了!')

    def do_hw(self, hw):
        print('我在做作業', hw)

    def study(self):
        print('我在讀書')
        self.score +=5

    def sleep(self):
        print('我在睡覺')

s1 = Student('John', 100)
s2 = Student('Allen', 95)
students = [s1, s2]

for s in students:
    print(s.name, '的分數是', s.score)

