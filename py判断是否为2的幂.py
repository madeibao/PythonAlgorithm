


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0

if __name__ == "__main__":
    s =Solution()
    n=4
    print(s.isPowerOfTwo((n)))

