

class Solution(object):
	def reverse(self,strs):
		i,j = 0,len(strs)-1	

		list2 =list(strs)
		while True:
			if i>j:
				break

			while list2[i] not in "aeiouAEIOU" and i<j:
				i+=1

			while list2[j] not in "aeiouAEIOU" and i<j:
				j-=1

			list2[i],list2[j] = list2[j],list2[i]
			i+=1
			j-=1

		return "".join(list2)

if  __name__ == "__main__":
	s = Solution()
	print(s.reverse("leetcode"))


