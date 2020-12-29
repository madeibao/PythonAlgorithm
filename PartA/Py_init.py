from dataclasses import dataclass
@dataclass
class A:
	x:int
	y:int
	def add(self):
		return self.x + self.y


c=A(3,5)
print(c.add())   # 上面的类的定义是python3.7的写法。


# -------------------------------------------------------------------
# -------------------------------------------------------------------


class Dog(object):
    def __init__(self):
        print("----init方法-----")

    def __del__(self):
        print("----del方法-----")

    def __str__(self):
        print("----str方法-----")
        return "对象的描述信息"

    # cls此时是Dog指向的那个类对象
    def __new__(cls):
        # print(id(cls))
        print("----new方法-----")
        return object.__new__(cls)


# print(id(Dog))

xtq = Dog()

