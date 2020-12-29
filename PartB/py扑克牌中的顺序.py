

# https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/
# 问能否构成顺子。
# 问能否构成顺子的牌数字。
# 问能否构成顺子。


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort() 
        for i in range(4):
            if nums[i] == 0: joker += 1
            elif nums[i] == nums[i + 1]: return False
        return nums[4] - nums[joker] < 5

if __name__ == "__main__":
    s =Solution()
    num2 = [1,2,3,4,5]
    num3 = [0,0,1,2,5]

