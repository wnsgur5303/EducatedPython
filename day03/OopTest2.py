class Dog:
    def __init__(self):
        self.back = True
    def muse(self):
        self.back = False
        
class Bird:
    def __init__(self):
        self.flypower = 100 
    def powerUp(self):
        self.flypower+=10
    def powerDown(self):
        self.flypower+=-10
    
class GaeSae(Dog,Bird):
    def __init__(self):
    #    super().__init__()
        Dog.__init__(self)
        Bird.__init__(self)
        
if __name__== '__main__':
    
#원래는 스크립트 언어라 읽어내려가는데 여기서 실행이 되면 여기가 메인이 된것이다.
#자바에 익숙하면 이걸쓰는경우가 있음
#코드리뷰..

    a = GaeSae()
    
    print(a.back)
    print(a.flypower)
    
    a.muse()
    
    a.powerUp()
    a.powerUp()
    a.powerUp()
    a.powerDown()
    
    print(a.back)
    print(a.flypower)
