

# 后缀表达式，利用栈来实现解法。

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        a = lambda m, n: n+m
        b = lambda m, n: n-m
        c = lambda m, n: n*m
        d = lambda m, n: int(n/m)

        dict2 = {
            "+": a,
            "-": b,
            "*": c,
            "/": d,
        }

        for t in tokens:
            if t in dict2:
                stack.append(dict2[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
        return stack.pop()

if __name__ == "__main__":
    s = Solution()
    str2 = ["2", "1", "+", "3", "*"]
    print(s.evalRPN(str2))



