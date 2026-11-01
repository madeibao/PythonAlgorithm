
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ca = 0
        cb = 0
        cc = 0

        for i in nums:
            if i == 0:
                ca += 1
            elif i == 1:
                cb += 1
            else:
                cc += 1
        
        for i in range(len(nums)):
            if i < ca:
                nums[i] = 0
            elif i < ca + cb:
                nums[i] = 1
            else:
                nums[i] = 2

        return nums

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    print(Solution().sortColors(nums))

    nums = [2,0,1]
    print(Solution().sortColors(nums))