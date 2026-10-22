

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(Solution().findMin(nums))  # 输出: 1