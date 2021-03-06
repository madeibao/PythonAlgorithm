




from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        f1 = lambda a,b:a+b
        f2 = lambda a,b:a-b
        f3 = lambda a,b:a*b
        f4 = lambda a,b:int(a/b)
        maps = {'+':f1,'-':f2,'*':f3,'/':f4}
        stack = []
        for i in tokens:
            if i in maps:
                a = stack.pop()
                b = stack.pop()

                # 注意调用的顺序问题。
                stack.append(maps[i](b,a))
            else:
                # i = int(i)
                stack.append(int(i))
        return stack[-1]


if __name__ == "__main__": 
	s = Solution()
	list2 =  ["2", "1", "+", "3", "*"]
	print(s.evalRPN(list2))

