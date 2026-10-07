class Solution(object):
    def legal(self, s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif stack and pairs[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        return not stack


if __name__ == '__main__':
    s = Solution()
    str2 = "()()[]{}"
    print(s.legal(str2))
