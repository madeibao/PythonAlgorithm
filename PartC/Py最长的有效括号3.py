

'''
import sys
 
def solve():
    khList = sys.stdin.readline().strip()
    length = len(khList)
    ret = [0] * length
    for i in range(1, length):
        if khList[i] == ')':
            j = i - ret[i - 1] - 1
            if j >= 0 and khList[j] == '(':
                ret[i] = ret[i - 1] + 2
                if j > 0:
                    ret[i] += ret[j - 1]
    print(max(ret))
     
if __name__ == '__main__':
    solve()


# 括号里面的值,最大的符合匹配规则的长度值。
# (()())

'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if stack and s[i] == ")":
                res.append(stack.pop())
                res.append(i)
            if s[i] == "(":
                stack.append(i)
        res.sort()
        # print(res)
        i = 0
        ans = 0
        n = len(res)
        while i < n:
            j = i
            while j < n - 1 and res[j + 1] == res[j] + 1:
                j += 1
            ans = max(ans, j - i + 1)
            i = j + 1
        return ans

'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res,i - stack[-1])
        return res
'''


if __name__ == "__main__":
	s = Solution()
	str2 = "(())"

	print(s.longestValidParentheses(str2))

