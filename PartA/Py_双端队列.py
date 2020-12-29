#coding=utf-8

# 双端队列

'''使用双端队列需要导入collections模块中的deque类。该类中提供了若干个方法用于操作双端队列，例如：
append方法可以将值添加到队列的尾部，而appendleft方法可以将值添加到队列的头部。pop方法可以弹出队列尾部的最后
一个值，并返回这个值。popleft方法可以弹出队列头部的第1个值，并返回这个值。'''

from collections import deque
#创建一个包含10个数字的双端队列
q = deque(range(10))
print(type(q)) # <class 'collections.deque'>
print(q) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 将100追加到双端队列q的队尾
q.append(100)
print(q) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
# 将-100追加到双端队列q的队尾
q.append(-100)
print(q) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, -100])
# 将20追加到双端队列q的队首
q.appendleft(20)
print(q) # deque([20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, -100])
# 弹出队尾的值
print(q.pop()) # -100
print(q) # deque([20, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
# 弹出队首的值
print(q.popleft()) # 20
print(q) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
# 将双端队列中的元素向左循环移动两个位置，也就是队首的元素会移动到队尾
q.rotate(-2)
print(q) # deque([2, 3, 4, 5, 6, 7, 8, 9, 100, 0, 1])
# 将双端队列中的元素向右循环移动两个位置，也就是队尾的元素会移动到队尾首
q.rotate(2)
print(q) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
# 创建一个双端队列q1
q1 = deque(['a','b'])
print(q1) # deque(['a', 'b'])
# 将q1追加到q的后面
q.extend(q1)
print(q) # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 'a', 'b'])
# 将q1追加到q的前面，这时q1会倒序排（先插第1个，再插第2个）
q.extendleft(q1)
print(q) # deque(['b', 'a', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 'a', 'b'])



