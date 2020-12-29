# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

# 示例 1:

# 输入: [3,0,1]
# 输出: 2


# 示例 2:

# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8




# 本质上还是一个等差数列的内容。
from typing import List


class Solution:
    def missingNumber(self, nums) -> int:
        sum = 0
        for i in nums:
            sum += i
        return len(nums) * (len(nums) + 1) // 2 - sum

	def missingNumber2(self, nums: List[int]) -> int:
	    if len(nums) == 0:
	        return None
	    nums.sort()
	    for i in range(0,len(nums)):
	        if nums[i] != i:
	            return i
	    return len(nums)


num3 = [3, 0, 1]
cc = Solution()
print(cc.missingNumber2(num3))







