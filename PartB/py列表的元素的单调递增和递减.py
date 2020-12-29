


# 严格的单调递增函数

def strictly_increasing(L):
    return all(x<y for x, y in zip(L, L[1:]))


# 严格的单调递减函数
def strictly_decreasing(L):
    return all( x>y for x, y in zip(L, L[1:]))


# 非严格的单调递增函数
def non_increasing(L):
    return all(x >= y for x, y in zip(L, L[1:]))


# 非严格的单调递减函数。
def non_decreasing(L):
    return all(x <= y for x, y in zip(L, L[1:]))


# 严格的单调递，每一个元素都小于后面的元素。
list2 = [1, 2, 3, 4, 5]

# 非严格单调增加，每一个元素都小于等于后面元素。
list3 = [1, 2, 2, 3, 4]
print(strictly_increasing(list2))
