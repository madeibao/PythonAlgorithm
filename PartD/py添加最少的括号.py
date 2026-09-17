class Solution:
    def minAddToMakeValid(self, bracket: str) -> int:
        stack = []
        for i in bracket:
            if stack:
                if stack[-1] == '(' and i == ')':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return len(stack)


if __name__ == '__main__':
    s = Solution()
    str2 = ")()"
    print(s.minAddToMakeValid(str2))
