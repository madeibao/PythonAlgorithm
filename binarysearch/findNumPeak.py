class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l = 0;
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l

# logN算法复杂度来求解山峰数组的索引位置

