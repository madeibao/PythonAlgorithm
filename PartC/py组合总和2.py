


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                dp[i] += dp[i - num]
        return dp[target]
                

if __name__ == "__main__":
	s = Solution()

	nums = [1,2,3]
	target = 4
	print(s.combinationSum4(nums, target))

	