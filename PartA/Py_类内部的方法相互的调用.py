__metaclass__ = type

class Stu:
    name = None
    age = None
    school = "华南理工大学"  # 类变量，被所有学生实例共有

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName_Age(self):
        print("我叫"+self.name+","+"今年"+str(self.age)+"岁。")

    def printSchool(self):
        print("来自", Stu.school)

    def printTotal(self):
        print("类中方法调用其他方法")
        Stu.printName_Age(self)
        Stu.printSchool(self)


stu = Stu("大哥", 19)
stu.printName_Age()
stu.printSchool()
print("*****类中函数调用其他函数********")
stu.printTotal()


# 其中Stu类的printTotal()函数有两种实现方法…

# 方法一
# 格式：类名.方法名(self)
# 注意：方法名内必须传入一个实例对象的指针,self后可根据方法定义放入适当实参

# 方法二
# 格式：self.方法名(方法列表)
# 方法列表不应该包括self
