




class Solution():
	def sumOfTwo(self,list2, target):
		i,j= 0, len(list2)-1

		while i<j:
			s = list2[i] + list2[j]

			if s>target:
				j-=1
			elif s<target:
				i+=1
			else:
				return [list2[i],list2[j]]

		return []


if __name__ == "__main__":
	s =Solution()
	list2 = [2,7,11,15]
	target = 9

	print(s.sumOfTwo(list2, target))

	