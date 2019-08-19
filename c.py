#class裡的function叫做method
#function間隔兩行，method間隔一行
#class裡的函示沒有順序差別
class Player:
    def __init__(self, name, ap):
        print('我誕生了')
        self.name = name
        self.hp = 100
        self.ap = ap

    def attack(self, target):
        print(self.name, '攻擊', target.name)
        target.hp -= self.ap

p1 = Player('Player1', 5)
p2 = Player('Player2', 10)
p1.attack(p2)
print(p2.hp)