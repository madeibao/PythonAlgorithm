


# 现场的复盘计算器的能力。
# # 从右向左遍历数组，将遍历过的数字维护到有序数组中，用二分查找的方式找到插入位置，也就是比当前数小的个数。

# 实现一个基本的计算器来计算一个简单的字符串表达式的值。

# 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

# 示例 1:

# 输入: "3+2*2"
# 输出: 7
# 示例 2:

# 输入: " 3/2 "
# 输出: 1
# 示例 3:

# 输入: " 3+5 / 2 "
# 输出: 5

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/basic-calculator-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def calculate(self, s: str) -> int:
        num,sign,stack = 0,'+',[]                 # 第一位为数字，所以初始化sign为'+'
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)          # 若有连续数字，如'1037'
            if ch in "+-*/" or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = ch                        # sign 记录ch 前一个符号。
        return sum(stack)
                

if __name__ == "__main__":
    s = Solution()
    s2 = "3+2*2"
    print(s.calculate(s2))

