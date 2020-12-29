from typing import List



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
        return nums
        


if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([1, 0, 2, 3, 0, 0, 23 ,32]))

