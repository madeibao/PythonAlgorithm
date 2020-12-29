


# 动态规划的思路
# 注意不能连续的打劫。


class Solution():
    def rob(self, nums):
        if len(nums)==0:
            return 0
        elif len(nums)<=2:
            return max(nums)

        dp = [nums[0], max(nums[0],nums[1])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i-2]+nums[i], dp[i-1]))
        return dp[len(nums)-1]


if __name__ == '__main__':

    s = Solution()
    print(s.rob([2, 7, 9, 3, 1]))








