python中的map()函数是一个内置的高阶函数，一般用法是map(function, iterable)。
需要传入一个函数，这个函数可以是内置的，也可以是自己定义，也可以是匿名函数。
第二个参数是一个可迭代对象，如列表，字符串等等。
返回的是一个map对象，注意不是列表不能直接输出，可以通过for循环或者list()来显示。
（python2返回的是列表）
不多说，直接上代码，一看就明白了。


def square(x):
    return x*x
a=map(square,[1,2,3]) 
print(a)        
#输出为<map object at 0x0033CFB0>   可以看出map返回的实际上是一个map对象
print(list(a))  
#输出为[1, 4, 9]   通过list（）方式 显示出来   

#也可以通过for循环来取出内容

ls=[]
for i in a:
    ls.append(i)
print(ls)
#输出为[1, 4, 9]


# 第二种情况

ls1='ABC'
ls2='abc'
print(list(map(lambda x,y:x+y,ls1,ls2)))
#['Aa', 'Bb', 'Cc']



# 第三种情况
# 若是传入的多个可迭代对象长度不相同，则按最短的长度进行处理(这是针对python3的)。具体用法如下：
ls1='ABC'
ls2='ab'
print(list(map(lambda x,y:x+y,ls1,ls2)))
#['Aa', 'Bb']




Map函数的应用详解

***将元组转换成list***
print(list(map(int, (1,2,3)))
[1, 2, 3]
***将字符串转换成list***
print(list(map(int, '1234')))
[1, 2, 3, 4]
***提取字典的key，并将结果存放在一个list中***
print(list(map(int, {1: 2, 2: 3, 3: 4})))
[1, 2, 3]
***字符串转换成元组，并将结果以列表的形式返回***
print(list(map(tuple, 'agdf')))
[('a',), ('g',), ('d',), ('f',)]
#将小写转成大写


def u_to_l (s):
  return s.upper()

print(list(map(u_to_l,'asdfd')))

['A', 'S', 'D', 'F', 'D']






#------------------------------------------------------------------
#------------------------------------------------------------------


numbers = [3, 2, 5, 1, 10, 7]


def square(x):
    return x*x

print(list(map(square,numbers)))
print([square(x) for x in numbers])   #列表的推导式来进行。

#----------------------------------------------------------------


[9, 4, 25, 1, 100, 49]
[9, 4, 25, 1, 100, 49]

















