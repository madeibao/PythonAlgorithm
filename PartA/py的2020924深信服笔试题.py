



from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    s =Solution()
    # list2 =[[1,3,5,9],
    #         [8,1,3,4],
    #         [5,0,6,1],
    #         [8,8,4,0],]

    res = []
    for i in range(16):
        a = int(input())
        res.append(a)

    res2 =[]
    for i in range(4):
        temp =res[:4]
        res = res[4:]
        res2.append(temp)

    print(s.minPathSum(res2))

