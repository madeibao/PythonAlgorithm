

# 一个矩阵中的发现一个单词的内容。
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, l = len(board), len(board[0]), len(word)
        used = [[0]*n for _ in range(m)]
        bias = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(c, r, location):
            nonlocal used
            flag = False
            # 判断当前字符是否匹配，若不匹配直接返回，剪枝操作
            if board[c][r]==word[location]:
                # 已匹配到最后一个字符且相同，返回True
                if location==l-1: return True
                # 当前字符字符匹配成功，后续递归过程中无法再次使用
                used[c][r] = 1
                # 对当前字符上下左右四个位置中未匹配的字符进行递归
                for dx, dy in bias:
                    x, y = c+dx, r+dy
                    if 0<=x<m and 0<=y<n and not used[x][y]:
                        flag = flag or dfs(x, y, location+1)
                # 回溯状态返回， 此字符可再次被使用
                used[c][r] = 0

            return flag
        # 遍历二维网格中的每一个字符
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0): return True
        return False




if __name__ == '__main__':
    s = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCC"
    print(s.exist(board, word))








