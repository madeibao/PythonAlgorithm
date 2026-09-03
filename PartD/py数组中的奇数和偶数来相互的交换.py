

# 数组中的奇数和偶数来进行相互的交换。

class Solution(object):
	def exchange(self,nums):
		i, j = 0,len(nums)-1

		while i < j:
			if nums[i]%2==0:
				i+=1
			elif nums[j]%2==1:
				j-=1
			else:
				nums[i],nums[j] = nums[j], nums[i]
				i+=1
				j-=1
		return nums


if __name__ == '__main__':
	s = Solution()
	nums = [1,2,3,4]
	print(s.exchange(nums))

