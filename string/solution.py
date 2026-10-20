
class Solution:
    def solveEquation(self, equation: str) -> str:

        def parse(string: str) -> tuple:
            i = 0
            n = len(string)
            conf = 0 # 前缀系数
            const = 0 # 常数项
            sign = 1 # 符号

            while i < n:
                if string[i] in "+-":
                    sign = 1 if string[i] == '+' else -1
                    i+=1
                else:
                    j = i
                    num = 0
                    has_num = False
                    while j < n and string[j].isdigit():
                        num = num * 10 + int(string[j])
                        has_num = True
                        j += 1
                    if j < n and string[j] == "x":
                            # 是 x 项
                        conf += sign * (num if has_num else 1)
                        j += 1
                    else:
                        # 是常数项
                        const += sign * num
                    i = j
            return conf, const

        left, right = equation.split("=")
        l_x, l_num = parse(left)
        r_x, r_num = parse(right)

        if l_x == r_x:
            return 'No solution' if l_num != r_num else 'Infinite solutions'
        else:
            return f'x={(r_num - l_num) // (l_x - r_x)}'


if __name__ == "__main__":
    str = Solution()
    print(str.solveEquation("x+5-3+x=6+x-2"))
    print(str.solveEquation("x=x"))
    print(str.solveEquation("2x=x"))
    print(str.solveEquation("2x+3x-6x=x+2"))
    print(str.solveEquation("x=x+2"))