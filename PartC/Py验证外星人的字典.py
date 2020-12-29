

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

    	dict2 = {}

    	if(len(order)!=26):
    		return False

    	if not words:
    		return False

    	for i in range(26):
    		dict2[order[i]] = chr(ord('a')+i)

    	new_words = []
    	for i in words:
    		temp = []
    		for j in i:
    			temp.append(dict2[j])
    		new_words.append("".join(temp))

    	for i in range(1, len(words)):
    		if words[i]>words[i-1]:
    			return False 
    	return True


if 	__name__ == "__main__":
	s = Solution()
	words = ["hello","leetcode"]
	order = "hlabcdefgijkmnopqrstuvwxyz"
	print(s.solve(words, order))
	