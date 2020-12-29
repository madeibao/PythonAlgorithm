


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))

        while i<=j:
            if c==i*i+j*j:
                return True
            elif i*i+j*j>c:
                j-=1
            else:
                i+=1
        return False


if __name__ == "__main__":
    s = Solution()
    num = 5
    print(s.judgeSquareSum(num))

    