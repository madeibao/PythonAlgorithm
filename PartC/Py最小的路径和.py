

# 最小的路径和结果
# 从左上角到右下角的得到的值是最小的结果
from typing import List

class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]



if __name__ == "__main__":
    s = Solution()  
    list2 = [[1,3,1],
             [1,5,1],
             [4,2,1]]
    print(s.minPathSum(list2))



# # 最大的路径和
# # 左上角和右下角的路径和为最小。
# # 牛妹的礼物，得到额体积为最小。
# 众所周知，牛妹有很多很多粉丝，粉丝送了很多很多礼物给牛妹，牛妹的礼物摆满了地板。
# 地板是N\times MN×M的格子，每个格子有且只有一个礼物，牛妹已知每个礼物的体积。
# 地板的坐标是左上角(1,1)  右下角（N, M）。
# 牛妹只想要从屋子左上角走到右下角，每次走一步，每步只能向下走一步或者向右走一步或者向右下走一步
# 每次走过一个格子，拿起（并且必须拿上）这个格子上的礼物。
# 牛妹想知道，她能走到最后拿起的所有礼物体积最小和是多少？
# 示例1
# 输入
# 复制
# [[1,2,3],[2,3,4]]
# 输出
# 复制
# 7
# 说明
# (1,1)->(1,2)->(2,3)
# 备注:
# 0<N,M<300
# 每个礼物的体积小于100

#----------------------------------------------------------------
class Solution(object):
    def selectPresent(self , presentVolumn ):
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


        for i in range(1,N):
            for j in range(1,M):
                dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+presentVolumn[i][j]
        return dp[i][j]


if __name__ == "__main__":
    s =Solution()
    list2 = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    print(s.selectPresent(list2))

