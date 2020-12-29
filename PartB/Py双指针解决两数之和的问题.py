
class Solution():
	def sumOfTwo(self,nums, target):

		i = 0
		j = len(nums)-1

		while i < j:
			temp = nums[i] +nums[j]
			if temp==target:
				return [l+1, r+1]

			elif temp>target:
				j-=1
			else:
				i+=1

		return []


if __name__ == "__main__":
	s = Solution()
	list2 =[2, 7, 9, 13]
	target = 9
	print(s.sumOfTwo(list2, target))

