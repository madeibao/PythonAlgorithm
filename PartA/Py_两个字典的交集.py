
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}


# 两个字典的交集的结果是一个集合， 所以用集合的形式来进行表示。
ss = set()
ss = a.keys() & b.keys()



