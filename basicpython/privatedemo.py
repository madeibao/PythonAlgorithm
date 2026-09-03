

# Python 中没有真正的私有属性和私有方法, 子类继承父类的变量和方法(非私有变量和方法)
class Car :
    def __init__(self, color, brand, model, price, owner):
        self.color = color
        self.brand = brand
        self.model = model
        self.price = price
        # __私有变量,外部无法直接访问,需要_Car__owner
        self.__owner = owner
    def start(self):
        print("车在跑")
    def run(self):
        print("车在跑")
    def stop(self):
        print("车在跑")
    #__私有方法,外部无法直接访问,需要_Car__control_fuel()
    def __control_fuel(self):
        print("正在加油")
    def get_owner(self):
        return self.__owner

if __name__ == "__main__":
    car = Car("red", "BMW", "X5", 100000, "张三")
    print(car.get_owner())
    car._Car__control_fuel()
