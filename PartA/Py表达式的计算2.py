


class Solution:# py3
    def calculate(self, s: str) -> int:
        sum, sign, num = 0, 1, 0
        stk = []
        for c in s:
            if c ==' ':
                continue
            if c =='+':
                sum += sign*num
                sign = 1
                num = 0
            elif c =='-':
                sum += sign*num
                sign = -1
                num = 0
            elif c =='(':
                stk.append(sum)
                stk.append(sign)
                sum, num = 0, 0
                sign = 1
            elif c ==')':
                sum += sign*num
                sum = sum*stk.pop()+stk.pop()
                num = 0
            else:
                num = num*10+int(c)
        return sum+sign*num



if __name__ == '__main__':
	str2 = "12+3+23+2-23+4+2 "
	s = Solution()
	print(s.calculate(str2))

