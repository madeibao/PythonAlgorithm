

# 求连续的子数组的最大的和。

class Solution(object):
    def maxSubSum(self,nums):
        
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)


if __name__ == "__main__":
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubSum(nums))






