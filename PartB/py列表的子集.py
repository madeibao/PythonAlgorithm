

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        N = len(nums)

        def helper(idx, temp_list):
            res.append(temp_list)

            for i in range(idx, N):
                helper(i+1, temp_list+[nums[i]])
        helper(0, [])
        return res

if __name__ == "__main__":
    s =Solution()
    print(s.subsets([1,2,3,4]))
    