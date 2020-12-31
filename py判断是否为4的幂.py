

# 固定的算法思想
# 如果 n <0 或者是 这个数字不是2的幂，肯定就不是4的幂

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if (num < 0 or num & (num-1)):
            return False
        
        return (num - 1) % 3 == 0

if __name__ == "__main__":
    s =Solution()
    n= 16
    print(s.isPowerOfFour((n)))

