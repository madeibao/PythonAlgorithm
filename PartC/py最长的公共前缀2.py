

class Solution(object):
	def longestprefix(self, strs):

		str2 =str()

		for i in zip(*strs):
			if len(set(i))==1:
				str2+=str(i[0])
		return str2

if __name__=='__main__':
	s= Solution()
	list2= ["flower","flow","flight"]
	print(s.longestprefix(list2))

