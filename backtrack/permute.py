

# 全排列算法

from typing import List

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        res = []
        length = len(nums)

        def backtrack(start):
            if start == length:
                res.append(nums.copy())
                return
            for i in range(start, length):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))

    