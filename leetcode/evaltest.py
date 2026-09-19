
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # token == "/"
                    stack.append(int(a / b))  # Use int() to truncate towards zero
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))
    print(s.evalRPN(["4", "13", "5", "/", "+"]))
    print(s.evalRPN(["10", "6", "9", "3", "/", "-", "*"]))

