
a = [1, 2, 3]
b = [4, 5, 6]
c = []
for i, j in zip(a, b):
    c.append(i*j)


print(c)

# [4, 10, 18]

# python的zip函数实现多个对象的遍历的操作。

# zip函数用来建立一个一一的映射关系。

lt4 = ['dd', '18', '183']
lt5 = ['name', 'age', 'height']
a = zip(lt5, lt4)

print(dict(a))


# {'age': '18', 'name': 'dd', 'height': '183'}

# https://github.com/objcoding/
list2 = [1, 2, 3, 4]
list3 = [2, 3, 2, 3]

list4 = []
for i, j in zip(list2, list3):
    list4.append((i, j))

m = []
n = []

for i in list4:
    m.append(i[0])
    n.append(i[1])

print(m)
print(n)


# [1, 2, 3, 4]
# [2, 3, 2, 3]



#----------------------------------------------------------------

zip函数还能够进行元组得分解

list2 = ["flower","flow","flight"]


for i in zip(*list2):
    print(i)

('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
('w', 'w', 'g')


#----------------------------------------------------------------

>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
 
>>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
>>>

 