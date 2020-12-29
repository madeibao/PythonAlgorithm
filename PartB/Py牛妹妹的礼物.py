

from typing import List

class Solution:
    def selectPresent(self, presentVolumn:List[List[int]]):
        # write code here
        if not presentVolumn:
            return 0

        N=len(presentVolumn)
        M=len(presentVolumn[0])

        dp=[[0]*M for _ in range(N)]
        dp[0][0]=presentVolumn[0][0]


        for i in range(1,N):
            dp[i][0]=dp[i-1][0]+presentVolumn[i][0]
        for i in range(1,M):
            dp[0][i]=dp[0][i-1]+presentVolumn[0][i]


        # 动态规划的值。
        for i in range(1,N):
            for j in range(1,M):
                dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+presentVolumn[i][j]
        return dp[i][j]
	# nums = [[1,2,3],[2,3,4]]

if __name__ == "__main__":
    s = Solution()
    nums = [[1,2,3],[2,3,4]]
    print(s.selectPresent(nums))


	