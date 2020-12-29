


import bisect
L = [1,3, 5, 7, 9, 11, 13, 15, 17,]
x = 10

pointer = bisect.bisect_left(L, x)

print(pointer)  # 5

pointer2 = bisect.bisect_right(L,x)

print(pointer2) # 5




