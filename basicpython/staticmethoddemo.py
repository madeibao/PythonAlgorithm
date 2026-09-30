
class User:
    @staticmethod
    def calc(a, b):
        return a + b

    def work(self):
        res = self.calc(10, 20)
        print(res)

    def multiply(self, a:int, b:int)->int:
        return a*b

    def work2(self):
        print(self.multiply(10,20))

if __name__== "__main__":
    User().work()
    
    print("----mutiply-------")
    User().work2()
    print(User.calc(20,30))

# static 方法调用案例

