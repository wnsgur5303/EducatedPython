from sqlalchemy.sql.expression import true
from rope.base.change import Change
class Animal:
    def __init__(self):
        self.age = 0
        self.egg = False
    def getOld(self):
        self.age+=1
    def ChangeEgg(self):
        self.egg = not self.egg
        
class Human(Animal):
    def __init__(self):
    #    super().__init__()
        Animal.__init__(self)
        self.moneypower = 11
    def makeMoney(self,earnmoney):
        self.moneypower += earnmoney
        

a = Human()
print(a.age)
print(a.egg)
print(a.moneypower)
a.getOld()
a.ChangeEgg()
a.makeMoney(100)
print(a.age)
print(a.egg)
print(a.moneypower)
#전역변수 만들기 (self 는 자바의 this)
#기본은 퍼블릭