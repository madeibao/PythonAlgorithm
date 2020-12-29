
# Python中没有像C++中public和private这些关键字来区别公有属性和私有属性
# 它是以属性命名方式来区分，如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，
# 否则为公有属性（方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）。

# Python 中虽然没有访问控制的关键字，例如 private、 protected 等等。但
# 是，在 Python 编码中，有一些约定来进行访问控制。

# 单下划线、 双下划线、 头尾双下划线说明：
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能
# 允许其本身与子类进行访问，不能用于 from module import *

# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类
# 本身进行访问了。

# __foo__: 头尾双下划线定义的是特列方法，类似 __init__() 之类的。


class Test(object):
    #私有方法
    def __test2(self):
        print("私有方法__test2方法")
    #普通方法
    def test(self):
        print("普通方法test")
    #普通方法
    def _test1(self):
        print("普通方法_test1方法")

        #可以在类内部调用私有方法
        t.__test2()#

        self.__test2()

t = Test()
t.test()
t._test1()

#t.__test2()和t.test2()#调用的时候会报错










