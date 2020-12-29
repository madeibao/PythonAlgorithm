
class Solution(object):
	def phonecompbination(self, strs):
		dict2 = {
					2:['a','b','c'],
					3:['d','e','f'],
					4:['g','h','i'],
					5:['j','k','l'],
					6:['m','n','o'],
					7:['p','q','r','s'],
					8:['t','u','v'],
					9:['w','x','y','z'],
				}

		if len(strs)==1:
			return dict2[int(strs)]

		temp = self.phonecompbination(strs[1:])

		res = []
		for i in temp:
			for j in (dict2[int(strs[0])]):
				res.append(i+j)
		return res


if __name__ == '__main__':
	s =Solution()
	str2 ="23"
	print(s.phonecompbination(str2))

