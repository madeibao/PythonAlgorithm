从它们的使用上来看,

@staticmethod不需要表示自身对象的self和自身类的cls参数(这两个参数都不需要添加），就跟使用函数一样。
使用：直接类名.属性名或直接类名.方法名。  # 直接类名，也可以直接类名()
@classmethod也不需要self参数, 但第一个参数需要是表示自身类的cls参数。
使用：直接类名.属性名或直接类名.方法名       # 直接类名，也可以直接类名()

# 直接定义一个test()函数

def test():
    print("i am a normal method!")


# 定义一个类，其中包括一个类方法，采用@staticmethod修饰
class T:

    @staticmethod
    def static_test():   # 没有self参数
        print("i am a static method!")


if __name__ == "__main__":
    test()
    T.static_test()
    T().static_test()


"""
i am a normal method!
i am a static method!
i am a static method!

"""
class T:
    @classmethod
    def class_test(cc):     # 必须有cls参数     #  这里第一个参数是cls， 表示调用当前的类名  cls,  用其他的变量名一样的可以。
        print("i am a class method")


if __name__ == "__main__":
    T.class_test()
    T().class_test()


# i am a class method
# i am a class method
