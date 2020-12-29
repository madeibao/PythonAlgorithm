

# 数字的补码
# 数字变成2进制后，0变成1，1变成0


class Solution:
    def findComplement(self, num: int) -> int:
        res = '0b'
        for bit in bin(num)[2:]:
            if bit == '1':
                res += '0'
            else:
                res += '1'
        return int(res, 2)

# 数学公式的算法。

class Solution:
    def findComplement(self, num: int) -> int:
        return 2**(len(bin(num))-2)-num-1

if __name__ == "__main__":
    s = Solution()
    num  = 2
    print(s.findComplement(num))
