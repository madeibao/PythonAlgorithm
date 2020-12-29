
operator模块输出一系列对应Python内部操作符的函数。
例如：operator.add(x, y)等价于表达式x+y。许多函数的名称都被一些特定的方法使用，没有下划线加持。
为了向下兼容，它们中的许多都保留着由双下划线的变体。那些不具备双下划线的变体是为了使表达更清晰。
这些函数在各种函数目录里扮演者对相比较、逻辑操作、数学运算以及序列操作等角色。
对于所有对象来讲对象比较函数是十分有用的，并且这些函数以它们支持的丰富的比较操作命名。


operator模块提供了一系列与Python自带操作一样有效的函数。
例如：operator.add(x, y)和表达式x+y是等效的。那些特殊类的方法都有自己的函数名；
为了方便起见，一些函数名是没有前导和后置（_）。 operator模块是用c实现的，所以执行速度比python代码快。

operator. lt(a, b)          //less than小于
operator. le(a, b)          //lessthan or equal to小于等于
operator. eq(a, b)          //equal to等于
operator. ne(a, b)          //not equal to不等于
operator. ge(a, b)          //greater and equal to大于等于
operator. gt(a, b)          //greater大于
operator. __le__(a, b)
operator. __lt__(a, b)
operator. __eq__(a, b)
operator. __ne__(a, b)
operator. __ge__(a, b)
operator. __gt__(a, b)





operator.itemgetter函数
operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号。看下面的例子
a = [1,2,3] 
>>> b=operator.itemgetter(1)      //定义函数b，获取对象的第1个域的值
>>> b(a) 
2
>>> b=operator.itemgetter(1,0)  //定义函数b，获取对象的第1个域和第0个的值
>>> b(a) 
(2, 1)
要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。
sorted函数用来排序，sorted(iterable[, cmp[, key[, reverse]]])
其中key的参数为一个函数或者lambda函数。所以itemgetter可以用来当key的参数
a = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
根据第二个域和第三个域进行排序
sorted(students, key=operator.itemgetter(1,2))






import operator
a = [1, 2, 3]
b = operator.itemgetter(1) 
c = operator.itemgetter(1, 0)   # 第一个域的第二个值。   第一个域的值可以为0,1,2 等三个值。
print(b(a))
print(c(a))  (2,2)




