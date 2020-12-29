

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

     	res = []
     	list2 = list(zip(s, indices))

     	res= sorted(list2,key=lambda x:x[1])
     	res2 = [x[0] for x in res]
     	return "".join(res2)


if __name__ == "__main__":
	s = Solution()
	s2 = "codeleet"
	indices = [4,5,6,7,0,2,1,3]
	print(s.restoreString(s2, indices))


