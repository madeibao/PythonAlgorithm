class Solution:
    def __init__(self):
        self.res = None

    def generateParenthesis(self, n: int) -> list[str]:
        self.res = []
        def backtrack(s, left, right, n):
            if left < 0 or right < 0 or left > n or right > n or right > left:
                return
            if len(s) == 2 * n:
                self.res.append(s)
                return
            backtrack(s + '(', left + 1, right, n)
            backtrack(s + ')', left, right + 1, n)
        backtrack('', 0, 0, n)
        return self.res


if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))
