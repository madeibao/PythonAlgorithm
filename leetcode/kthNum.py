
from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        nums.sort(key=lambda x: int(x), reverse=True)
        return nums[k - 1]

if __name__ == "__main__":
    sol = Solution()
    nums = ["3", "6", "7", "10"]
    k = 4
    print(sol.kthLargestNumber(nums, k))  # Output: "3"

