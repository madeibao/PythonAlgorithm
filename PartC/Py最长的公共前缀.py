



# python求出最长的公共前缀。

class Solution(object):
	def maxLength(self,nums):
		s= str()
		for i in zip(*nums):
			if len(set(i))==1:
				s+=i[0]
			else:
				break
		return s


if __name__=='__main__':
	list2 = ["apple", "applist","append","appmmm"]

	s = Solution()
	print(s.maxLength(list2))

