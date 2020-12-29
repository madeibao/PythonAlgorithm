


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        f1 = lambda a, b: b+a
        f2 = lambda a, b: b-a
        f3 = lambda a, b: b*a
        f4 = lambda a, b: int(b/a)

        dict2 = {"+": f1, "-": f2, "*": f3, "/": f4}
        stack = []

        for i in tokens:
            if i in dict2:
                a = stack.pop()
                b = stack.pop()
                stack.append(dict2[i](a,b))
            else:
                stack.append(int(i))
        return stack[-1]


if __name__ == "__main__":
    s = Solution()
    list2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(s.evalRPN(list2))
