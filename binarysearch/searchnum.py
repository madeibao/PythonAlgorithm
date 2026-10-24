

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        # 左边界：第一个 >= target
        # 右边界：第一个 > target 的前一个位置

        left_index = self.bound(nums, target)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]

        # 右边界：第一个 > target 的前一个位置, 因为左边界已经找到了，所以这里可以直接用 target + 1 来找右边界
        right_index = self.bound(nums, target + 1) - 1
        return [left_index, right_index]
        
    # 寻找第一个 >= target 的位置
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
