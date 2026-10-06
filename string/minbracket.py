

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            elif stack[-1] == '(' and s[i] == ')':
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)


if __name__ == '__main__':
    str = "(((";
    print(Solution().minAddToMakeValid(str))