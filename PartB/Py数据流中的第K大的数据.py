

import heapq

class KthLargest(object):
    def __init__(self, k, nums):

        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for i in nums:
            self.add(i)
    def add(self, val):

        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        return self.heap[0]


if __name__ == "__main__":
    k = 2
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, ]
    s = KthLargest(k, num)
    print(s.add(6))