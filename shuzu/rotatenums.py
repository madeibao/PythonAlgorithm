
class Solution:
    def helper(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.helper(nums,0,k-1)
        self.helper(nums,k,len(nums)-1)
        self.helper(nums,0,len(nums)-1)

if __name__=="__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    s=Solution()
    s.rotate(nums, k)
    print(nums)