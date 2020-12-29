

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:

    	dp1 =[0 for _ in range(len(ratings))]
    	dp2 =[0 for _ in range(len(ratings))]


    	for i in range(1, len(ratings)):
    		if ratings[i]>ratings[i-1]:
    			dp1[i] = dp1[i-1] +1


    	for i in range(len(ratings)-2, -1, -1):
    		if ratings[i]>ratings[i+1]:
    			dp2[i] = dp2[i+1] +1

    	sum2 =0
    	for i in range(len(ratings)):
    		sum2 += max(dp1[i],dp2[i])
    	return sum2
if __name__ == "__main__":
	s = Solution()
	list2 = [1,2,3]	
	print(s.candy(list2))

	