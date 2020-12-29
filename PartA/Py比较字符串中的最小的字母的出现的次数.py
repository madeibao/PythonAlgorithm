
# leetcode 1170

from typing import List
from collections import Counter


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    	list2 = []
    	list3 = []

    	for i in range(len(queries)):
    		list2.append(self.countNum(queries[i]))

    	for j in range(len(words)):
    		list3.append(self.countNum(words[j]))


    	res = []

    	for i in range(len(list2)):
    		count =0
    		for j in range(len(list3)):
    			if list2[i]<list3[j]:
    				count +=1
    		res.append(count)
    	return res

    	
    def countNum(strs):
    	temp = "".join(sorted(strs))
    	dict2 = dict(Counter(temp))

    	res = 0
    	for k,v in dict2.items():
    		if k==temp[0]:
    			res =v
    	return res 

if __name__ == "__main__":
	s = Solution()
	queries = ["bbb", "cc"]	
	words = ["a","aa","aaa","aaaa"]
	print(s.numSmallerByFrequency(queries,words))



