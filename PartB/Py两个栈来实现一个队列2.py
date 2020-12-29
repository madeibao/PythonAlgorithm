

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.help = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.help)==0:
            while(len(self.queue)!=0):
                self.help.append(self.queue.pop())
        return self.help.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.help)==0:
            while(len(self.queue)!=0):
                self.help.append(self.queue.pop())

        # 只是返回结果值，并不会真正的弹出。
        return self.help[-1]
    

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.queue)==0 and len(self.help)==0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()



