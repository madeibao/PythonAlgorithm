


def climb():
    n = int(input())
    if n == 0 or n == 1:
        return n
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


print(climb())



# 依照列表的形式来进行存储兔子的增长的数列。

def climb():
    list2 = [0, 1, 1, ]
    n = int(input())
    if n == 0 or n == 1:
        return n
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
        list2.append(b)
    return list2


print(climb())
