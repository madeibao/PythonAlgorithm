
from typing import List

class Solution:
    def minDistinctFreqPair(self, nums: List[int]) -> List[int]:
        
        count = {}
        for w in nums:
            count[w] = count.get(w, 0) + 1
        res = []
        for i in count:
            for j in count:
                if count[i]!=count[j]:
                    res.append([i,j])

        if res:
            res.sort(key=lambda x: (x[0],x[1]))
            return res[0]
        return [-1,-1]


if __name__=="__main__":
    nums = [1,1,4,3]
    print(Solution().minDistinctFreqPair(nums))


# python 的多条件排序算法
        