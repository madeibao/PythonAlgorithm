
from typing import List, Tuple



class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort() 
        for i in range(4):
            if nums[i] == 0: joker += 1
            elif nums[i] == nums[i + 1]: return False
        return nums[4] - nums[joker] < 5


if __name__ == "__main__":
    s = Solution()
    list2 = [0,0,3,4,5]
    print(s.isStraight(list2))

    