

class MaxQueue:
    def __init__(self):
        self.queue=[]

        
    def max_value(self) -> int:
        if len(self.queue)==0:
            return -1
        else:
            return max(self.queue)

    def push_back(self, value: int) -> None:
        self.queue.append(value)


    def pop_front(self) -> int:
        if len(self.queue)==0:
            return -1
        else:
            return self.queue.pop(0)






