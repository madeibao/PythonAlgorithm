

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')   # 异或的操作。

cc = Solution()
print(cc.hammingDistance(2, 4))


# 输入: x = 1, y = 4
# 输出: 2

# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑



