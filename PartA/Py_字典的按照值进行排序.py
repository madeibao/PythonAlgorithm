

words = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5}   # 字典的按照值进行排序。
print(words)



sort = sorted(words.items(), key=lambda e: e[1])   				 # 生成一个列表。
sort = sorted(words.items(), key=lambda e: e[1], reverse=True)   # 逆序的方式來生成一个列表
print(sort)


# e[1] 代表的是按照值進行排序，


for key, value in sort:
    print(str(key)+" "+str(value))  # 中间设置空格的形式，

# 一个字典的输出中，按照字典的值，排序之后，进行打印。

# {'a': 1, 'd': 4, 'c': 3, 'f': 5, 'b': 2}
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('f', 5)]
# a 1
# b 2
# c 3
# d 4
# f 5











