一种著名的数据结构是堆（heap），它是一种优先队列。优先队列让你能够以任意顺序添加对象，
并随时（可能是在两次添加对象之间）找出（并删除）最小的元素。相比于列表方法min，这样做的效率要高得多。
实际上，Python没有独立的堆类型，而只有一个包含一些堆操作函数的模块。
这个模块名为heapq（其中的q表示队列），它包含6个函数，其中前4个与堆操作直接相关。必须使用列表来表示堆对象本身。

                                                                             模块heapq中一些重要的函数
                                                               函 数                                              描 述
                                                      heappush(heap, x)                                        将x压入堆中
                                                        heappop(heap)                                      从堆中弹出最小的元素
                                                        heapify(heap)                                           让列表具备堆特征
                                                  	 heapreplace(heap, x)                            弹出最小的元素，并将x压入堆中
                                                      nlargest(n, iter)                                       返回iter中n个最大的元素
                                                     nsmallest(n, iter)                                   返回iter中n个最小的元素
#=----------------------------------------------------------------------------------------

from random import shuffle
from heapq import *

data = list(range(10))
shuffle(data)   # 打乱顺序的结果值。
heap = []

for n in data:
    heappush(heap, n)

print(heappop(heap))


#----打印结果值。
#---
[0, 1, 2, 4, 3, 8, 9, 7, 6, 5]
0



函数heapreplace用得没有其他函数那么多。它从堆中弹出最小的元素，再压入一个新元素。
相比于依次执行函数heappop和heappush，这个函数的效率更高。
>>> heapreplace(heap, 0.5) 
0     # 返回的是弹出的元素的内容。
>>> heap 
[0.5, 1, 5, 3, 2, 7, 9, 8, 4, 6] 




函数heapify通过执行尽可能少的移位操作将列表变成合法的堆（即具备堆特征）。
如果你的堆并不是使用heappush创建的，应在使用heappush和heappop之前使用这个函数。
尽快的变成一个堆的形式和结果值。
heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(heap)
print(heap)


[0, 1, 5, 3, 2, 7, 9, 8, 4, 6]   


#============================================================================

import heapq


heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapq.heapify(heap)

print("n个最大的数据是")
print(heapq.nlargest(3, heap))








