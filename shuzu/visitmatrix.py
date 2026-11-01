

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        
        m = len(mat)
        n = len(mat[0])

        res = []
        diago = 0 # 斜对角线数，从0开始递增
        element = 0

        while element < m * n:
            if diago % 2 == 0:
                i = min(diago, m - 1)
                j = diago - i
                while i >= 0 and j < n:
                    res.append(mat[i][j])
                    element += 1
                    i -= 1
                    j += 1
            else:
                j = min(diago, n - 1)
                i = diago - j
                while j >= 0 and i < m:
                    res.append(mat[i][j])
                    element += 1
                    i += 1
                    j -= 1

            diago += 1
        return res


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().findDiagonalOrder(mat))

    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().findDiagonalOrder(mat))