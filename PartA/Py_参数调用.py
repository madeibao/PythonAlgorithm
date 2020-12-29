1.带一个星号（*）参数的函数传入的参数存储为一个元组（tuple）
2.带两个星号（*）参数的函数传入的参数则存储为一个字典（dict），并且再调用是采取a=1,b=2,c=3的形式
3.传入的参数个数不定，所以当与普通参数一同使用时，必须把带星号的参数放在最后。
4.函数定义的时候，再函数的参数前面加星号，将传递进来的多个参数转化为一个对象，一个星号转换成元组，两个星号转换成字典，相当于把这些参数收集起来
5.参数前加一个星号，将传递进来的参数放在同一个元组中，该参数的返回值是一个元组
6.参数前两个星号，将传递进来的参数放到同一个字典中，该参数返回值为一个字典


def tuple_pack(a, *b):
    print(a)
    print(b)


tuple_pack(1, 2, 3, 4, 5)   # 元组的打包



# 1
# (2, 3, 4, 5)

def dictionary_pack(a, **b):
    print(a)
    print(b)

dictionary_pack(1,one=1,two=2,three=3,four=4)  # 字典的打包。

# 1
# {'three': 3, 'four': 4, 'one': 1, 'two': 2}


def tuple_dictionary_pack(*args , **kwargs):
    print(args)
    print(kwargs)


tuple_dictionary_pack(1, 2, 3, one=2, two=2)


# (1, 2, 3)
# {'two': 2, 'one': 2}