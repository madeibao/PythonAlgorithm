

from typing import List, Tuple


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        res = []
        def dfs(index):
            if index == len(nums):
                res.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                dfs(index + 1)
                nums[i], nums[index] = nums[index], nums[i]
        dfs(0)
        return res

if __name__ == "__main__":
    s =Solution()
    list2 =[1,2,3]
    print(s.permute(list2))

    