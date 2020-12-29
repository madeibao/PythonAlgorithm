
根据逆波兰表示法，求表达式的值。
有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
说明
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：
输入: [“2”, “1”, “+”, “3”, “*”]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：
输入: [“4”, “13”, “5”, “/”, “+”]
输出: 6
解释: (4 + (13 / 5)) = 6
示例 3：
输入: [“10”, “6”, “9”, “3”, “+”, “-11”, “", “/”, "”, “17”, “+”, “5”, “+”]
输出: 22
解释:
((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


#=============================================================

class Solution():
    def getResult(self,tokens):
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "/":
                    num = b // a
                    if (num < 0) and (b % a != 0):
                        stack.append(num + 1)
                    # 注意这里，如果b不能整除a，且小于零，根据取整原理，
                    # 要在b//a的基础上加1。
                    # 如6/-100,取整的话应该等于0.但是6//-100是等于-1的，
                    # 因此要在6//-100 的基础上加1.
                    else:
                        stack.append(num)
                elif i=="*":
                    stack.append(b*a)
                elif i=="+":
                    stack.append(b+a)
                elif i=="-":
                    stack.append(b-a)
        return stack.pop()

# 解法二:

class Solution():
    def getResult(self,tokens):
        f1 = lambda a,b:a+b
        f2 = lambda a,b:a-b
        f3 = lambda a,b:a*b
        f4 = lambda a,b:int(a/b)

        map2 = {'+':f1, '-':f2, '*':f3, '/':f4}
        stack = []

        for i in tokens:
            if i in map2:
                a = stack.pop()
                b = stack.pop()
                stack.append(map2[i](a,b))
            else:
                stack.append(int(i))
        return stack.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.getResult(["4", "13", "5", "/", "+"]))






    