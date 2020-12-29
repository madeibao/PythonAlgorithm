

通过字典来进行统计列表中的结果值

bag = ['apple', 'orange', 'cherry', 'apple','apple', 'cherry', 'blueberry']
count = {}
for fruit in bag:
    count[fruit] += 1
print(count)

# ==================================================================
# ===================================================================


Traceback (most recent call last):
  File "E:/pythonWorkSpace/TensorTest/Test.py", line 10, in <module>
    count[fruit] += 1
KeyError: 'apple'

通过其中的结果，发现，每次运行，都会有指针的错误

2. 使用判断语句检查
因此，在单词第一次被统计时，需要在count中给每个键设定一个默认值1，这可以用一个判断语句来实现：


bag = ['apple', 'orange', 'cherry', 'apple','apple', 'cherry', 'blueberry']
count = {}
for fruit in bag:
    if fruit not in count:
        count[fruit] = 1
    else:
        count[fruit] +=1

print(count)


# -------------------------------------------------------------------
# 当然也可以使用defaultdict字典的写法

from collections import defaultdict
count = defaultdict(int)

bag = ['apple', 'orange', 'cherry', 'apple','apple', 'cherry', 'blueberry']
for fruit in bag:
	count[fruit] += 1

# ================================
# 更加简洁的方法内容/

for fruit in bag:
	count[fruit] = count.setdefault(fruit, 0) + 1


3. 使用dict.setdefault()方法
dict.setdefault(key[,default])方法接受两个参数，第一个是键的名称，第二个参数是默认值。
在调用时如果键存在字典中，
会返回它的值；如果不存在，则会自动把它添加进字典中并返回默认值，
default的默认值为None。此外，default的值还可以是列表，元组，集合和字典等。

>>> d = {'a': 1, 'b': 2}
>>> d.setdefault('a')    #键存在并返回他的值
1
>>> d.setdefault('c', 3)     #添加键-值
3
>>> d.setdefault('d')    #只添加键，默认值为None
>>> d
{'a': 1, 'b': 2, 'c': 3, 'd': None}









