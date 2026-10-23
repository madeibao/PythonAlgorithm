

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []
        deq = deque()
        res = []
        for i in range(len(nums)):
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            if deq[0] == i - k:
                deq.popleft()

            if i >= k - 1:
                res.append(nums[deq[0]])
        return res


if __name__=='__main__':
    s = Solution()
    list2 = [1, 3, -1, -3, 5, 3, 6, 7]
    print(s.maxSlidingWindow(list2, 3))


