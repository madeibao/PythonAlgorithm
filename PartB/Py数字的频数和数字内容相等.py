

from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:

    	counts = dict()
    	for i in arr:
    		counts[i] = counts.get(i, 0) + 1

    	res = []
    	for i in counts.keys():
    		if counts[i]==i:
    			res.append(i)

    	if len(res)!=0:
    		return max(res)
    	else:
    		return -1


if __name__ == "__main__":
	s = Solution()
	list2 = [2,2,3,4]
	print(s.findLucky(list2))

