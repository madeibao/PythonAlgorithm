
第一种情况。
a, b, c = map(int, input().split())  	 # 这条语句就能够表示输入的句法。
#  表示的是一次能够输入多个值，依照空格进行分割。
a, b, c = map(int, input(),split(","))   # 这种情况是按照逗号进行分割。

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
































