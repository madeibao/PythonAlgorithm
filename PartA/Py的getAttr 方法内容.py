Python的hasattr() getattr() setattr() 函数使用方法详解 


（一） hasattr(object,name) 函数 
判断一个对象里面是否有 name 属性或者 name 方法，返回 bool 值，如果有 name 属性（方法）则返回 True ，否则返回 False 。注意： name 需要使用引号括起来。 
class function_demo(object):
    name = 'demo'
    def run(self):
       return "hello function"
 
functiondemo = function_demo()
print(hasattr(functiondemo, 'name')) #判断对象是否有 name 属性，True
print(hasattr(functiondemo, "run")) #判断对象是否有 run 方法，True
print(hasattr(functiondemo, "age")) #判断对象是否有 age 属性，False
（二） getattr(object,name[,default]) 函数 
获取对象 object 的属性或者方法，若存在则打印出来；若不存在，则打印默认值，默认值可选。
注意：如果返回的是对象的方法，那么打印的结果是方法的内存地址。如果需要运行这个方法，那么可以在后面添加括号 () 。 
class function_demo(object):
    name = 'demo'
    def run(self):
       return "hello function"
 
functiondemo = function_demo()
print(getattr(functiondemo, 'name')) #获取 name 属性，存在就打印出来--- demo
print(getattr(functiondemo, "run"))
# 获取 run 方法，存在打印出方法的内存地址
# <bound method function_demo.run of <__main__.function_demo object at 0x006E8A10>>
 
# print(getattr(functiondemo, "age"))
# 获取不存在的属性，报错如下：
# Traceback (most recent call last):
#   File "F:/Python/PycharmProjects/Mytest_code/tmp.py", line 11, in <module>
#     getattr(functiondemo, "age")
# AttributeError: 'function_demo' object has no attribute 'age'
 
print(getattr(functiondemo, "age", 18)) #获取不存在的属性，返回一个默认值
（三） setattr(object,name,values) 函数 
给对象的属性赋值，若属性不存在，则先创建再赋值。 
class function_demo(object):
     name = 'demo'
     def run(self):
       return "hello function"
functiondemo = function_demo()
 
print(hasattr(functiondemo, 'age'))# 判断 age 属性是否存在，False
setattr(functiondemo, 'age', 18 ) #对 age 属性进行赋值，无返回值
print(hasattr(functiondemo, 'age')) #再次判断属性是否存在，True
综合使用：
class function_demo(object):
name = 'demo'
def run(self):
  return "hello function"
 
functiondemo = function_demo()
 
if hasattr(functiondemo, 'addr'):# 先判断是否存在
    addr = getattr(functiondemo, 'addr')
    print(addr)
else:
    addr = getattr(functiondemo, 'addr', setattr(functiondemo, 'addr', '首都北京'))
    #addr = getattr(functiondemo, 'addr', '美国纽约')
    print(addr)
运行结果：首都北京。 





