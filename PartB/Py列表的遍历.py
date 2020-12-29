方法一：最简单常用的，用for遍历列表
list = [2, 3, 4]

for num in list:
    print(num)


输出： 
2
3
4
#----------------------------------------------------------------




方法二：利用python内置函数enumerate（）列举出list中的数

enumerate(sequence, [start=0])，返回枚举对象

参数

sequence -- 一个序列、迭代器或其他支持迭代对象。
	start -- 下标起始位置。
 用法实例

list = [2, 3, 4] 
for i in enumerate(list):     
	print(i)

输出： 
0 2
1 3
2 4
#----------------------------------------------------------------




方法三：使用iter（）迭代器

iter(object[, sentinel]) 函数用来生成迭代器，返回迭代对象。

参数

object -- 支持迭代的集合对象。
	sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象（如，函数），此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象的__next__()方法时，都会调用 object。
用法实例

list = [2, 3, 4]
for i in iter(list):
	print(i)

输出： 
2
3
4
#----------------------------------------------------------------




方法四：使用range（）函数

pytho range(start, stop[, step]) 函数返回类型是ndarray，可用list（）返回一个整数列表，一般用在 for 循环中。

参数

start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
	end: 计数到 end 结束，但不包括 end。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
	step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
用法实例



list = [2, 3, 4]
for i in range(len(list)):
	print(i, list[i])


 输出： 
 0 2
 1 3
 2 4
