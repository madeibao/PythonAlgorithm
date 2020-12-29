
leetcode64 的测试的题目内容。
一个矩阵从左上角的元素到右下角的元素的最短的路径值。

class Solution:
    #def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid) -> int:
        if not grid:
            return None
        for m in range(1,len(grid)):   # 代表的是行数
            grid[m][0]+=grid[m-1][0]
        
        for n in range(1,len(grid[0])): # 代表的是列数。
            grid[0][n]+=grid[0][n-1]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i and j:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]

m, n = map(int, input().split())     # 这条语句就能够表示输入的句法。

# 在这里M是行数字，N是列数字。
A = m*[0*n]

for i in range(m):
    A[i] = input().split(" ")
    for j in range(n):
        A[i][j] = int(A[i][j])

cc = Solution()
print(cc.minPathSum(A))


按照如下的格式进行输入：

3 3
1 3 1
1 5 1
4 2 1