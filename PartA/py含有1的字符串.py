


import itertools

class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        for _, j in itertools.groupby(s):
            print(list(j))
    
        return 0


if __name__ == "__main__":
    s = Solution()
    s2 = "0110111"
    print(s.numSub(s2))


