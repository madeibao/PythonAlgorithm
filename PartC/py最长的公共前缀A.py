


class Solution(object):
	def longestPrefix(self, strs):
		res = ""
		for i in zip(*strs):
			if(len(set(i))==1):
				res+=i[0]
			else:
				break
				
		return res

if __name__ == "__main__":
	s = Solution()
	list2= ["flyght","flower","fly"]
	print(s.longestPrefix(list2))




