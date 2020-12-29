


class Solution(object):
	def move(self,strs):
		dict2 = {}

		for i in str:
			temp = "".join(sorted(list(i)))
			if i in dict2:
				dict2[temp].append(i)
			else:
				dict2[temp].append([i])
		return list(dict2.values())



if __name__ == "__main__":
	s = Solution()
	list2 = [""]