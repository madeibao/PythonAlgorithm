


# 删除排序的数组中的重复的元素，然后返回长度值。


class Solution(object):
	def remove(self, nums):
		i = 0

		while i<len(nums)-1:
			if nums[i] == nums[i+1]:
				nums.remove(nums[i])
			else:
				i +=1

		return len(nums)



if __name__ == "__main__":
	s = Solution()
	print(s.remove([1, 1, 2])

