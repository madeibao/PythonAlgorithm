
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
    	if n<=0 or k>n or k<=0:
    		return []

    	res = []
    	self.__dfs(0, n, k,[], res)
    	return res

    def __dfs(self,start, n, k, temp, res):

    	if len(temp) == k:
    		res.append(temp[:])
    		return 

    	for i in range(start, n+1):
    		temp.append(i)
    		self.__dfs(i+1, n, k, temp, res)
    		temp.pop()



if __name__ == "__main__":
	s = Solution()
	n =4 
	k =2
	print(s.combine(n,k))




