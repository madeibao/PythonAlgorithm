
# 理论上数字4幂的二进制类似于100，10000，1000000，etc...形式。可以有如下结论：
# 4的幂一定是2的。
# 4的幂和2的幂一样，只会出现一位1。但是，4的1总是出现在奇数位。
# 0x5 = 0101b可以用来校验奇数位上的1。




class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0 or num & (num-1):					# num&(num-1) 用来判断是否为2的幂指数。
            return False
            
        # return (num - 1) % 3 == 0
        return (num & 0x55555555) != 0

cc = Solution()
print(cc.isPowerOfFour(32))



# 0b01010101010101010101010101010101  二进制的表示情况为 0x55555555
# 0b00000000000000000000000000010000












