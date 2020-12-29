


# 判断是否为合法的括号的。

class Solution:
    def isValid(self, s: str) -> bool:
        stack, d = [], {'{': '}', '[': ']', '(': ')'}
        for p in s:
            if p in '{[(':
                stack += [p];
            elif not (stack and d[stack.pop()] == p):
                return False
        return not stack


if __name__ == '__main__':
	s= Solution()
	str2 = "()()"
	print(s.isValid(str2))

