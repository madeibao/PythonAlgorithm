
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0

        def dfs(index:int, current_sum:int):
            if index == len(nums):
                if current_sum == target:
                    self.count += 1
                return

            # Choose the current number with a positive sign
            dfs(index + 1, current_sum + nums[index])
            # Choose the current number with a negative sign
            dfs(index + 1, current_sum - nums[index])

        dfs(0, 0)
        return self.count

if __name__ == '__main__':

    nums = [1, 1, 1, 1, 1]
    target = 3
    print(Solution().findTargetSumWays(nums, target))  # Output: 5


