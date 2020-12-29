

import itertools

class Solution:
    def maxPower(self, s: str) -> int:

    	res = 0

    	for _,j in itertools.groupby(s):
    		list2 = len(list(j))
    		if list2>res:
    			res =list2
    		else:
    			continue

    	return res
