

from typing import List
import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        sorted_nums = []
        for i in range(len(nums) - 1, -1, -1):
            idx = bisect.bisect_left(sorted_nums, nums[i])  # 二分查找，Python自带的函数
            ans.append(idx)
            sorted_nums.insert(idx, nums[i])
        
        return ans[::-1]


if __name__ == "__main__":
    s = Solution()
    list2 = [5,2,6,1]
    print(s.countSmaller(list2))

    