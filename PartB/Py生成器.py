现在有个需求，看列表 [0，1，2，3，4，5，6，7，8，9]，要求你把列表里面的每个值加1，你怎么实现呢？
方法一（简单）：

info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []
# for index,i in enumerate(info):
#     print(i+1)
#     b.append(i+1)
# print(b)
for index,i in enumerate(info):
    info[index] +=1
print(info)
#================================================================
方法二：
info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = list(map(lambda x:x+1,info))
print(a)
for i in a:
    print(i)

方法三：高级版本的内容。

info = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [i+1 for i in range(10)]
print(a)

#=================================================================
# python的生成器的内容。
通过列表生成式，我们可以直接创建一个列表，但是，受到内存限制，列表容量肯定是有限的，而且创建一个包含100万个元素的列表，
不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
从而节省大量的空间，在Python中，这种一边循环一边计算的机制，称为生成器：generator

生成器是一个特殊的程序，可以被用作控制循环的迭代行为，python中生成器是迭代器的一种，使用yield返回值函数，每次调用yield会暂停，
而可以使用next()函数和send()函数恢复生成器。
生成器类似于返回值为数组的一个函数，这个函数可以接受参数，可以被调用，
但是，不同于一般的函数会一次性返回包括了所有数值的数组，生成器一次只能产生一个值，这样消耗的内存数量将大大减小，
而且允许调用函数可以很快的处理前几个返回值，因此生成器看起来像是一个函数，但是表现得却像是迭代器

#----------------------------------------------------------------
python的生成器内容

要创建一个generator，有很多种方法，第一种方法很简单，只要把一个列表生成式的[]中括号改为（）小括号，就创建一个generator
举例如下：

#列表生成式
lis = [x*x for x in range(10)]
print(lis)
#生成器
generator_ex = (x*x for x in range(10))
print(generator_ex)
 
结果：
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
<generator object <genexpr> at 0x000002A4CBF9EBA0>    # 代表的是对象。

如果要一个个打印出来，可以通过next（）函数获得generator的下一个返回值：

# 生成器
generator_ex = (x*x for x in range(10))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
print(next(generator_ex))
# 结果：
0
1
4
9
16
25
36
49
64
81
Traceback (most recent call last):
 
  File "列表生成式.py", line 42, in <module>
 
    print(next(generator_ex))
 
StopIteration

大家可以看到，generator保存的是算法，每次调用next(generaotr_ex)就计算出他的下一个元素的值，
直到计算出最后一个元素，没有更多的元素时，抛出StopIteration的错误，
而且上面这样不断调用是一个不好的习惯，正确的方法是使用for循环，因为generator也是可迭代对象：

# 应该下面的这种写法才能够十分的稳妥。
#生成器
generator_ex = (x*x for x in range(10))
for i in generator_ex:
    print(i)
     
结果：
0
1
4
9
16
25
36
49
64
81
所以我们创建一个generator后，基本上永远不会调用next()，而是通过for循环来迭代，
并且不需要关心StopIteration的错误，generator非常强大，如果推算的算法比较复杂，
用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

# 著名的是斐波那契数列的内容。
def fib(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b =b,a+b
        n = n+1
    return 'done'
 
a = fib(10)
print(fib(10))  # 
# <generator object fib at 0x000001C03AC34FC0>

# 完整的程序内容。
def fib(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b =b,a+b
        n = n+1
    return 'done'
 
a = fib(10)
print(fib(10))
print(a.__next__())
print(a.__next__())   # 调用一次，返回的是一次的值。
print(a.__next__())
print("可以顺便干其他事情")
print(a.__next__())
print(a.__next__())
 
结果：
<generator object fib at 0x0000023A21A34FC0>
1
1
2
可以顺便干其他事情
3
5

#另一种写法内容。
#================================================================

在上面fib的例子，我们在循环过程中不断调用yield，就会不断中断。
当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：
def fib(max):
    n,a,b =0,0,1
    while n < max:
        yield b
        a,b =b,a+b
        n = n+1
    return 'done'
for i in fib(6):
    print(i)
     
结果：
1
1
2
3
5
8





