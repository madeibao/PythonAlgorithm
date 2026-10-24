

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        left_index = self.bound(nums, target)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]

        right_index = self.bound(nums, target + 1) - 1
        return [left_index, right_index]
        

    def bound(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    print(Solution().searchRange(nums, target))
