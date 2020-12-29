


# 过滤掉其中的字符的结果值。

'''  $bo*y gi!r#l #  '''

s= input()

list2 = list(filter(lambda x:x.isalnum(),s))
print(list2)


['b', 'o', 'y', 'g', 'i', 'r', 'l']
lambda 的后面是一个可以迭代的对象结果


