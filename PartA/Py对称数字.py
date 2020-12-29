 

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false


#----------------------------------------------------------------
#----------------------------------------------------------------


class Solution(object):
	def isSpecial(self,num):
		dic2 = {'6':'9','0':'0','1':'1','8':'8','9':'6'}

		list2 = list(num)
		i = 0
		j = len(list2)-1


		for i in range(0, j//2):
			if dic2[list2[i]] != list2[j-i]:
				return False
		return True

if __name__ == '__main__':
	s = Solution()
	s2 = "9696"

	print(s.isSpecial(s2))