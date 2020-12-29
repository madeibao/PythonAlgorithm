


第一种情况。
a, b, c = map(int, input().split())  	 # 这条语句就能够表示输入的句法。
#  表示的是一次能够输入多个值，依照空格进行分割。
a, b, c = map(int, input().split(","))   # 这种情况是按照逗号进行分割。

print(a)
print(b)
print(c)


第二种情况
对于含有空格的一行数的输入
list1 = list(map(int, input().split()))
list1 = list(map(int, input().split(",")))  按照逗号进行分割。
输入的形式为 23 23 23 242   中间按照空格进行分割。
# 一次性的输入n个数据，并且保存到列表中。
# 如果取第几个数，就是用列表的指针的形式
第一个数：list1[0]
第二个数：list1[1]
第三个数：list1[2]


第三种情况
b = input().split()  # 依次输入这些数据。  # 这样也可以一次的输入一些数据。

ll = []              # 创建列表。
for i in b:
    ll.append(eval(i))
print(ll)

输入的形式为  3 3 232 23 24 324 
输出的结果为 [3, 3, 232, 23, 24, 324]   用列表来进行存储。


输入一串数字，按照空格进行分割，并且转化为列表的形式来进行存储。

array = list(map(int, input().strip().split(" ")))   # 去除空格的分割内容。
print(array)

输入的形式为
23 23 24 1 23 4 323 44 2 23 
[23, 23, 24, 1, 23, 4, 323, 44, 2, 23]


第四种情况

对于先输入个数n ，后输入n个数的情况（用循环）

n = int(input())
li = []
for i in range(n):
    b = int(input())
    li.append(b)
    
print(li)

按照下面的格式进行输入：
4 # 输入的是4个数据
1
2
3
4

一定要回车和换行。
然后[1,2,3,4]




第五种情况：
4.保证list里面的数全为整数
b = ['1', '2', '4']
b = [int(i) for i in b]
print(b)

结果：
[1,2,4]

当然也可以采用的是map函数来解决问题：

b = ['1', '2', '4']
b = list(map(int, b))
print(b)

[1,2,4]



第六种情况
a = ['1', '2', '3', '4']
print(' '.join(a))
输出结果为  1 2 3 4 

若要求输出格式为  1,2,3,4
print(’,’).join(a)



第七种情况

输入一个整型值，代表的是字符串的长度。
然后输入对应长度的字符串。

num =int(input())
str=input()



第八种情况
n = input().split(",")   # 一个字符串接收两个输入，然后用逗号分割开来。
例如 输入 "1432219,3"


n0 = n[0]  # 接收的结果为  1432219
n1 = n[1]  # 接收的结果为  3

n0 = str(n0)
print(n0)
print(n1)



第九种情况：
输入一个数字，代表的是n个测试用例。
然后再输入这些测试用例。

例如输入两个字符串测试用例：
2
hello 
woooooooow
可以得到如下代码


for i in range(int(input())):
    s = input()


例如输入一个数字代表的是n个测试用例
然后用列表存储这些测试用例

list1 = []
for i in range(int(input())):
    s = int(input())
    list1.append(s)

print(list1)



第10种情况
对于首先输入一个数据，代表的是n个测试用例
然后输入n个用例的例子
例如：

2
19:90:23
23:59:59

# n个测试用例。
# 用下划线来直接的表示n个测试的用例，在里面进行循环的操作。

n = int(input().strip())  #代表n个数字
for _ in range(n):
	HH, MM, SS = map(int, input().strip().split(':'))





第11种情况
import sys

a=sys.stdin.readline().strip()
b=input()
print(len(a),len(b))


执行结果：
abc
abc
3 3


第12种情况：

a = list(map(int, input().strip().split()))   # 转换成列表的形式来进行存储。

print(min(a))


按照如下的形式来进行输入：

23 23 23 21 12 2 4 13 133 13 1 1233 13 2323 4 23





互联网笔试的输入。

#----------------------------------------------------------------
#----------------------------------------------------------------


1. 一行输入
1.1 输入一个数/字符串
一行输入如果输入只有一个数或者一个字符串的话，直接使用input读取就可以了


s = input()

print(s)



1.2 输入一个数组
输入一个数组的话和输入一个数类似，只不过需要使用split()分解一下

s = input()
s = [i for i in s.split()]
print(s)


2. 两行输入
两行读取要在一行读取的基础上再进行一些操作。
这里举个例子，假设第一行输入数组长度，第二行输入数组，那么读入操作分两步，首先获得数组长度，然后获取数组。


while True:

    s = input()

    if s != "":

        length = int(s)

        nums = [int(i) for i in input().split()]

        print(length, nums)

        break

    else:

        break



3. 多行输入
3.1 每行输入一个数/字符串
如果每行只输入一个数或者字符串的话这种情况直接使用while循环和input进行读取。



while True:

    s = input()

    if s != "":

        print(s)

    else:

        break


3.2 每行读取不同内容
有的时候题目要求每行内容输入不同，举个例子，第一行输入操作个数，从第二行还是输入n个数组。


data = []

length = int(input())

n = 0

while n < length:

    s = input()

    if s != "":

        temp = [i for i in s.split()]

        data.append(temp)

        n = n + 1

    else:

        break

print(data)



#----------------------------------------------------------------


while True:
	n = int(input('Please input a number:\n'))
	sn = list(map(int,input('Please input some numbers:\n').split()))
	print(n)
	print(sn,'\n')


#-----------------------------------------------------------------------
import sys
try:
    while True:
        print('Please input a number:')
        n = int(sys.stdin.readline().strip('\n')) #strip('\n')表示以\n分隔，否则输出是“字符串+\n”的形式
        print('Please input some numbers:')
        sn = sys.stdin.readline().strip()#若是多输入，strip()默认是以空格分隔，返回一个包含多个字符串的list。
        if sn == '':
            break
        sn = list(map(int,sn.split())) #如果要强制转换成int等类型，可以调用map()函数。
        print(n)
        print(sn,'\n')
except:
    pass


# ---------------------------------------------------------------
# --------------------------------------------------------------
# ----------------------------------------------------------------
import sys

while True:
    n = sys.stdin.readline().strip()
    if n == '':
        break
    n = int(n)
    line = sys.stdin.readline().strip()
    item = list(map(int, line.split()))




