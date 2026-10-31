
import collections

class MyStack:
    def __init__(self):
        self.queuea = collections.deque()
        self.queueb = collections.deque()

    def push(self, x: int) -> None:
        self.queueb.append(x)
        while self.queuea:
            self.queueb.append(self.queuea.popleft())
        self.queuea, self.queueb = self.queueb, self.queuea

    def pop(self) -> int:
        return self.queuea.popleft()

    def top(self) -> int:
        return self.queuea[0]

    def empty(self) -> bool:
        return not self.queuea;


if __name__ == '__main__':
    stack = MyStack()

    stack.push(1)
    stack.push(2)
    print(stack.top())

    print(stack.empty())


