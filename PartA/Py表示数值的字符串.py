

# 判断数值表示是否为数字的合法表示。

class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif char == '.':
                if met_dot or met_e: return False
                met_dot = True
            elif char == 'e' or char == 'E':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit

if __name__ == '__main__':
    s = Solution()

    a, b, c,d, e = "+100","5e2","-123","3.1416","-1E-16"
    print(s.isNumber(a))
    print(s.isNumber(b))
    print(s.isNumber(c))
    print(s.isNumber(d))
    print(s.isNumber(e))

