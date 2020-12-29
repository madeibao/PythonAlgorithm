

from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        list2 = list(set(A[0]))
        res = []	

        for i in list2:
        	minNum =min(a.count(i) for a in A)
        	res.append(minNum*i)
        return res

        
if __name__ == "__main__":
	s = Solution()
	list2 =["bella","label","roller"]
	print(s.commonChars(list2))
