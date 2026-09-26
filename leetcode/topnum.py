
from typing import List

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hp = []
        res = Counter(nums)
        
        # build a max heap using negative values to simulate a max heap with min heap
        for key, value in res.items():
            hp.append((-value, key))
            
        heapq.heapify(hp)
        result = []
        for _ in range(k):
            _, val = heapq.heappop(hp)
            result.append(val)
        return result


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
