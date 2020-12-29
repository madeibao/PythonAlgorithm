class Rectangle():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def getPeri(self):
        return (self.a + self.b)*2
    def getArea(self):
        return self.a * self.b
 
rect = Rectangle(3,4)
print(rect.getPeri())
print(rect.getArea())
print(rect.__dict__)


#==----------------------------------------------------------------

14
12
{'b': 4, 'a': 3}
