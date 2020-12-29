

class Solution:
    def rotatedDigits(self, N: int) -> int:
        dic2 = {'0': '0', '1': '1','2':'5','5':'2','6':'9','8':'8','9':'6'}
        res = 0
        for i in range(1, N+1):
            temp = str()
            for j in str(i):
                if j not in dic2:
                    break
                else:
                    temp = temp + dic2[j]
            if len(temp) ==len(str(i)) and temp!= str(i):
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    N = 10
    print(s.rotatedDigits(N))
