



import itertools


def getmultiply(A, B):
    list2 = []
    for x in itertools.product(A, B):
        list2.append(x)

    return list2


print(getmultiply([1, 2, 3], [4, 5]))



# [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]




