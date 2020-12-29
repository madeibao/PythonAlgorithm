

from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

print(queue.popleft())
print(queue.pop())  		# 弹出最右端的方法。
print(queue)



# Eric
# deque(['John', 'Michael', 'Terry', 'Graham'])











