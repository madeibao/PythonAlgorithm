
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic2 = dict(Counter(nums))
        sort = sorted(dic2.items(), key=lambda e: e[1], reverse=True)
	
        res = []
        for i in range(k):
            res.append(sort[i][0])
        return res 



if __name__ == "__main__":
    s = Solution()
    list2 = [-1,-1]
    k =1 #
    print(s.topKFrequent(list2, k))

