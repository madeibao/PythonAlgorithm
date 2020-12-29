
# 每一个数字都是3，5，7的倍数
# 1 3 5 7 9

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        x3,x5,x7=0,0,0
        result = [1]
        for _ in range(1,k):
            result.append(min(3*result[x3],5*result[x5],7*result[x7]))
            if result[-1] == 3*result[x3] : x3+=1
            if result[-1] == 5*result[x5] : x5+=1
            if result[-1] == 7*result[x7] : x7+=1
        return result[-1] 


if __name__ == "__main__":
    s = Solution()
    k = 5
    print(s.getKthMagicNumber(k))

