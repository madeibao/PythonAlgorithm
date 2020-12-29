class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        num1 = text.count('b')
        num2 = text.count('a')
        num3 = text.count('l')
        num4 = text.count('o')
        num5 = text.count('n')

        # print(num1)
        # print(num2)
        # print(num3)
        # print(num4)
        # print(num5)

        numN = min(min(num1, num2), num5)
        numM = min(num3, num4)

        num8 = numM //2
        
        numsum = min(numN, num8)

        return numsum


if __name__ == "__main__":
    s = Solution()
    print(s.maxNumberOfBalloons("loonbalxballpoon"))