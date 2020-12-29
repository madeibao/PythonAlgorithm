
# intervals = [[1,3],[2,6],[8,10],[15,18]]



class Solution(object):
	def merge(self,intervals):
		if len(intervals)==0:
			return []
		res = []

		# 首先按照第一个数字来进行排序。
		intervals.sort(key = lambda x:x[0])
		for inter in intervals:
			if len(res)==0 or res[-1][1]<inter[0]:
				res.append(inter)
			else:
				res[-1][1] =  max(res[-1][1], inter[1])
		return res


if __name__ == "__main__":
	s = Solution()
	intervals = [[1,3],[2,6],[8,10],[15,18]]
	print(s.merge(intervals))

# [[1, 6], [8, 10], [15, 18]]
