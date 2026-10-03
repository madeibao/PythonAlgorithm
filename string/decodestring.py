
class Solution:
    def decodeString(self, s: str) -> str:
        
        res = ""
        stack = []
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((res, num))
                res = ""
                num = 0
            elif c == "]":
                last_res, repeat_num = stack.pop()
                res = last_res + res * repeat_num
            else:
                res += c
        return res
    
if __name__ == "__main__":
    s = "3[a]2[bc]"
    solution = Solution()
    result = solution.decodeString(s)
    print(result)  # Output: "aaabcbc"