



class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()



if __name__ == "__main__": 
	c = CQueue()
	c.appendTail(1)
	c.appendTail(2)
	print(c.deleteHead())
	