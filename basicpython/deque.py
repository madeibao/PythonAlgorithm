

from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack[-1])  # Output: 3

print(stack.pop())  # Output: 3

print(stack)  # Output: deque([1, 2])


