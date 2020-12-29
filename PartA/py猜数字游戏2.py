

from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:  

        countA = 0
        countB = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                countA += 1

        dictA = dict(Counter(secret))
        dictB = dict(Counter(guess))


        for i in dictA:
            if i in dictB:
                countB += min(dictA[i], dictB[i])

        countB = countB - countA
        return str(countA) + "A"+ str(countB) + "B"


if __name__ == "__main__":
    s = Solution()
    secret = "1123"
    guess = "0111"

    print(s.getHint(secret,guess))

