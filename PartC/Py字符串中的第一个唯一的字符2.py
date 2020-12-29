class Solution:
    def firstUniqChar(self, s: str) -> int:

    	dic2 = {}
    	list2 = list(s)

    	for c in list2:
    		dic2[c] = dic2.get(c, 0) +1


    	for c in list2:
    		if dic2[c]==1:
    			return c
    			


if __name__ == "__main__":
	s = Solution()
	print(s.firstUniqChar("leetcode"))

