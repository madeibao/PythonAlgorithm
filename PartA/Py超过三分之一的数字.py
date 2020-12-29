
# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

# 示例 1:
# 输入: [3,2,3]
# 输出: [3]
# 示例 2:

# 输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]



class Solution(object):
	def majorityElement(self,nums):
		n = len(nums)
		dic = {}	
		for x in nums:
			if x in dic:
				dic[x] += 1
			else:
				dic[x] = 1

		return [x for x in dic.keys() if dic[x]>n/3]


if __name__ == "__main__":
	s = Solution()
	print(s.majorityElement([1,1,1,3,3,2,2,2]))

