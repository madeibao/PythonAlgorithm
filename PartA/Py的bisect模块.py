在平时使用python对list进行操作时，有时候会遇到这种情况：
我们想要向一个已经排序好的list插入新元素，但不想改变原list的顺序，
也就是说新元素的目标是插入到符合原list顺序的位置
（比如数字2作为新元素被插入list[1,    3, 4]后，list应变成[1, 2, 3, 4]）,bisect模块刚好可以实现这个简单的需求。

bisect 模块用于维护有序列表。
其实现了一个算法用于插入元素到有序列表。较为准确来说，它采用二分法来排序插入。

bisect 返回要插入元素在列表中的下标。假定列表是有序的。
bisect_left 与 bisect 类似，只不过其默认将元素插到左边，所以返回的是插入到左边的下标
bisect_right与 bisect_left 相反。
以上方法若列表无序，那么会返回插入到列表最后一个合适的位置。
insort 会在列表中插入元素到正确位置，假定列表有序。如果列表无序，那么会返回空。默认插入到右边。
insort_left 和insort_right 类似。



NOTE: 使用这个模块必须先保证之前的列表是有序的


bisect返回你要插入的数据的位置
bisect_left 该函数用入处理将会插入重复数值的情况，返回将会插入的位置,
bisect_right 该函数用入处理将会插入重复数值的情况，返回将会插入的位置
insort 插入 在不改变原有数据的情况下插入到重复值的右边
insort_left 插入到重复值的左边
insort_right 插入到重复值的右边


当你决定使用二分搜索时，这个模块会给你带来很大的帮助。



NOTE: 使用这个模块必须先保证之前的列表是有序的
import bisect
L = [1,3,3,6,8,12,15]
x = 3


# 在L中查找x，x存在时返回x左侧的位置，x不存在返回应该插入的位置..这是3存在于列表中，返回左侧位置１
x_insert_point = bisect.bisect_left(L, x)
print(x_insert_point)   # 返回1


# 将x插入到列表L中，x存在时插入在左侧
x_insort_left = bisect.insort_left(L, x)
print(L)  # [1,3,3,3,6,8,12,15]

# 将x插入到列表L中，x存在时插入在右侧
x_insort_rigth = bisect.insort_right(L, x)
print(L)  # [1, 3, 3, 3, 3, 6, 8, 12, 15]


#--------------------------------------------------------

bisect
​ —— 其实bisect 就是在调用 bisect_right

import bisect

li = [1, 23, 45, 12, 23, 42, 54, 123, 14, 52, 3]
li.sort()
print(li)
print(bisect.bisect(li, 3))





insort

—— 在列表a中插入元素x，并在排序后保持排序。如果x已经在a中，把它插入到x的右边。



import bisect

li = [1, 23, 45, 12, 23, 42, 54, 123, 14, 52, 3]
li.sort()
print(li)
bisect.insort(li, 3.0)
print(li)


[1, 3, 12, 14, 23, 23, 42, 45, 52, 54, 123]
[1, 3, 3.0, 12, 14, 23, 23, 42, 45, 52, 54, 123]12

​—— 其实insort 就是在调用 insort_right







