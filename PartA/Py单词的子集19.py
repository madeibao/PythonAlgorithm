



from typing import List
from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
    	res = []
    	countB = [Counter(i) for i in B]

    	max_dict = {}

    	for i in countB:
    		for k, v in i.items():
    			max_dict[k] = max(max_dict.get(k, 0), v)


    	for i in A:
    		CountA = Counter(i)

    		for k, v in max_dict.items():
    			if v>CountA.get(k, 0):
    				break
    		else:
    			res.append(i)

    	return res

if __name__ == "__main__":
    s = Solution()
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["lo", "eo"]
    print(s.wordSubsets(A,B))

