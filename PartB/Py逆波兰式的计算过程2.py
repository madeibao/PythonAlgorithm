

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#================================================================


class Solution():
	def evalTest(self,token):
		operator = ["+", "-", "/","*"]
		res = []

		if len(token)==0:return 0
		else:
			for c in token:
				if c not in operator:
					res.append(c)
				else:
					a = int(res.pop())
					b = int(res.pop())
					if c=="+":
						res.append(str(a+b))
					elif c=="-":
						res.append(str(a-b))
					elif c=="*":
						res.append(str(a*b))
					elif c=="/":
						res.append(str(int(a/b)))
		return res[0]

if __name__ == "__main__":	
	s = Solution()
	list2 = ["2", "1", "+", "3", "*"]
	print(s.evalTest(list2))
	