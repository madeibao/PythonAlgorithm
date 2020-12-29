

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
    	dict2 = {}
    	if len(order)!=26:
    		return False

    	if not words:
    		return False

    	for i in range(26):
    		dict2[order[i]] = chr(ord('a')+i)

    	res =[]

    	for word in words:
    		temp = []
    		for i in word:
    			temp.append(dict2[i])

    		res.append("".join(temp))

    	for j in range(1,len(res)):
    		if res[j]<res[j-1]:
    			return False
    	return True

if __name__ == "__main__":
	s =Solution()
	words = ["hello","leetcode"]
	order = "hlabcdefgijkmnopqrstuvwxyz"
	print(s.isAlienSorted(words, order))

