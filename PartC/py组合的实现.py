


# 组合公式的实现
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        res = []

        def backtrack(res, path, m):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(m, n + 1):
                path.append(i)
                backtrack(res, path, i + 1)
                path.pop()

        backtrack(res, path, 1)
        return res


if __name__ == "__main__":
    s = Solution()
    n = 4
    k = 2
    print(s.combine(n, k))





