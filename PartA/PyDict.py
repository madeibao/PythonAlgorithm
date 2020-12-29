
# python创建字典的方法

dic = {}
print(type(dic))  # dict类型，创建一个空字典。




# 通过zip函数创建字典。
dic = dict(zip('abc', [1, 2, 3]))
print(dic)
# {'a': 1, 'c': 3, 'b': 2}


# 直接赋值创建字典。
dic = {'spam':1, 'egg':2, 'bar':3}
print(dic)


# 通过关键字dict和关键字的参数来创建。
dic = dict(spam = 1, egg = 2, bar =3)
print(dic)

# {'bar': 3, 'egg': 2, 'spam': 1}

# 通过二元组列表来创建字典。
list = [('spam', 1), ('egg', 2), ('bar', 3)]
dic = dict(list)
print(dic)


# 通过字典的推导式子来创建。
dic = {i: 2*i for i in range(3)}
print(dic)  # {0: 0, 1: 2, 2: 4}


# 通过dict.fromkeys()创建

dic = dict.fromkeys(range(3), '33')
print(dic)

# {0: '33', 1: '33', 2: '33'}




ment = dict()  # 简单的语句创建一个空字典。
ment['a'] = 2
ment['b'] = 3
ment['c'] = 4
print(ment)







