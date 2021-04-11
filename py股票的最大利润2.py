

from typing import List


class Solution(object):
	def maxProfit(self, prices: List[int]) -> int:

		if len(prices)==0:
			return 0

		profit = -float("inf")
		temp = prices[0]

		for i in range(1, len(prices)):
			temp = min(temp, prices[i])
			profit = max(profit,prices[i]-temp)
		return profit


if __name__ == "__main__": 
	s = Solution()
	nums = [7,1,5,3,6,4]
	print(s.maxProfit(nums))





