


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(list1), 0, -2):
    print(i)


# 逆序的输出，注意的是，最终的结果包括0.
# 淡然也可是是-1

for i in range(len(list1), -2, -2):
    print(i)


# 这样只能取下标值，但是无法用列表的指针，list1[i],这种情况会报指针的越界。

for i in reversed(range(10)):
    print(i)

# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0