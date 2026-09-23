
from typing import List

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        length = len(nums)
        def dfs_back(start, path):
            res.append(path.copy())
            for i in range(start, length):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                dfs_back(i + 1, path + [nums[i]])   
        
        dfs_back(0, [])
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 2]
    print(solution.subsetsWithDup(nums))