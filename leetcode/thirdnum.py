

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        if len(list(set(nums))) < 3:
            return max(set(nums))
        list2 = list(set(nums))
        list2.sort(reverse=True)
        return list2[2]

if __name__ == '__main__':
    nums = [3, 2, 1]
    print(Solution().thirdMax(nums))
