
from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        i = nums.index(1)
        j = nums.index(n)
        return i + (n - 1 - j) - (1 if i > j else 0)

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 2]
    print(sol.semiOrderedPermutation(nums))

    nums = [2, 1, 4, 3]
    print(sol.semiOrderedPermutation(nums))

