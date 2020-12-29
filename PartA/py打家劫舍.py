
# 围成一圈房屋的打家劫舍的勾当。
# 打家劫舍的勾当的第二种方式。
# 打家劫舍的升级的版本结果。


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums[0], nums[1])
        
        def rob_action(nums):
            length = len(nums)
            dp = [0 for _ in range(length)]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, length):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp
        
        # 去掉第一间
        nums1 = nums[1:]
        dp1 = rob_action(nums1)
        # 去掉最后一间
        nums2 = nums[:-1]
        dp2 = rob_action(nums2)


        return max(dp1[-1], dp2[-1])


if __name__ == "__main__":
    s =Solution()
    list2 = [2,3,2]
    print(s.rob(list2))

    





