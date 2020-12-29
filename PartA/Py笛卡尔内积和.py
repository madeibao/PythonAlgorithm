



import itertools


def getmultiply(A, B):
    list2 = []
    sum2 = 0
    for x in itertools.product(A, B):
        x = list(x)
        list2.append(x)
    for i in list2:
        sum2 += i[0]*i[1]

    return sum2


print(getmultiply([1, 2, 3], [4, 5]))  # 54
