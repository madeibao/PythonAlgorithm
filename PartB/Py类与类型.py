
class Foo:
    pass

obj=Foo()

print(isinstance(obj,Foo))        #判断一个对象是否是由某个类调用产生

# 在python3中统一类与类型的概念
d={'x':1} #d=dict({'x':1} #)    #类即类型，d是一个对象，dict是一个类，d是由调用dict产生的对象

print(type(d) is dict)          #type也可以判断数据类型，但这并不是type的的主要功能，其实type是一个元类
print(isinstance(d,dict))





