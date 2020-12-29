class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, n, n, '')
        return res
        
    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')


if __name__ == '__main__': 
    s = Solution()
    res = s.generateParenthesis(3);
    print(res)




from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(l, r, s):
            if l > n or r > n: return
            if (l == r == n): res.append(s)
            if l < r: return
            # 加一个左括号
            dfs(l + 1, r, s + '(')
            # 加一个右括号
            dfs(l, r + 1, s + ')')
        dfs(0, 0, '')
        return res


if __name__ == '__main__':
    s = Solution()
    n =4
    print(s.generateParenthesis(n))
