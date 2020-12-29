
#===================================================================================================================================
1
2
3
4
5
6
7
8
8
7
6
5
4
3
2
1

输入结果
22
#---------------------------------------------------------------------------------------------------------------------------------------------------	

class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0: continue
                elif i == 0:  grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:  grid[i][j] = grid[i - 1][j] + grid[i][j]
                else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]


if __name__ == '__main__':
    s = Solution()

    res = []
    for i in range(16):
        res.append(int(input()))

    res2 = []
    for i in range(4):
        temp = res[:4]
        res =res[4:]
        res2.append(temp)

    print(s.minPathSum(res2))

