


class Solution(object):
	def kthFrequent(self,list2):

		dict2 = {}

		for i in list2:
			dict2[i] = dict2.get(i,0) +1
		return dict2



if __name__ == "__main__":
	s = Solution()
	list2 =[1,1,1,2,2,3]
	print(s.kthFrequent(list2))

	