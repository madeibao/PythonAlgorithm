




# 原地的删除一些元素，并且返回的是删除元素之后的列表的大小。

class Solution(object):
	def delete(self,nums, target):

		idx = 0
		for i in range(len(nums)):
			if nums[i] != target:
				nums[idx]= target
				idx+=1
		return idx

if __name__ == "__main__":
	s = Solution()
	list2 = [2,3,3,2]
	target = 2
	print(s.delete(list2, target))

