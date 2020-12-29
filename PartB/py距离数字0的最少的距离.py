


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return
        row, col = len(matrix), len(matrix[0])
        dist = [[float("inf")] * col for _ in range(row)] # 初始化一个较大值 确保矩阵会被更新
        # 找0的位置


        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    dist[i][j] = 0 # 0到0本身的距离为0

        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序

        # 从左上角的位置上开始计算
        for i in range(row):
            for j in range(col):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)


        # 从右下角的位置上开始计算
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                if i + 1 < row:
                    dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j + 1 < col:
                    dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
        return dist


if __name__ == "__main__":
	s= Solution()

	list2 = [[0,0,0],
			 [0,1,0],
			 [0,0,0]]

	print(s.updateMatrix(list2))

