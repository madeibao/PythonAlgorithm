
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """ 

        m = len(board)  # 行数
        n = len(board[0]) if m > 0 else 0  # 列数

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'E'  # Mark as escaped
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        

        # Mark all 'O's on the border and connected to border as 'E'
        for i in range(m):  
            dfs(i, 0)        # Left border
            dfs(i, n - 1)    # Right border
        
        for j in range(n):
            dfs(0, j)        # Top border
            dfs(m - 1, j)    # Bottom border

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # Flip surrounded 'O' to 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'  # Restore escaped 'O' back to 'O'
        
if __name__ == '__main__':
    s = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    s.solve(board)
    for row in board:
        print(row)





