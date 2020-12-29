
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append('(')
            else:
                if stack[len(stack)-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    a = stack.pop()
                    temp = 0
                    while a != '(':
                        temp += a
                        a = stack.pop()
                    stack.append(2*temp)
        return sum(stack)


class Solution(object):
    def scoreOfParentheses(self, S):
        deep, res = 0, 0
        for i in range(len(S)):
            if S[i] == "(":
                deep += 1
            else:
                deep -= 1
            if S[i] == ")" and S[i-1] == "(":
                res += 2**deep
        return res

if __name__ == '__main__':
    str2 = "(())"
    s = Solution()
    print(s.scoreOfParentheses(str2))



