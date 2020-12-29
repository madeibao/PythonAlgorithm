

class Solution(object):
    def maxprofit(self,nums):

        # 利润为极小值。
        if len(nums)==0:return 0
        
        maxprofit = -float("inf")
        temp = nums[0]

        for i in range(1, len(nums)):
            temp = min(temp, nums[i])
            maxprofit = max(maxprofit, nums[i]-temp)
        return maxprofit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices)==0:return 0
        maxprofit = 0
        temp = prices[0]

        for x in range(1, len(prices)):
            temp = min(temp, prices[x])
            maxprofit = max(maxprofit,nums[x]-temp)
        return maxprofit


if __name__ == "__main__":
    s = Solution()
    nums = [7,1,5,3,6,4]
    nums2 = [7,6,4,3,1]
    print(s.maxprofit(nums))
    print(s.maxprofit(nums2))




    