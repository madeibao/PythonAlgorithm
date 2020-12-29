


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


if  __name__ == "__main__":


	# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
	# [[],[1],[2],[],[],[]]
	queue2 = MaxQueue()
	queue2.push_back(1)
	queue2.push_back(2)
	print(queue2.max_value())
	queue2.pop_front()
	print(queue2.max_value())

	


