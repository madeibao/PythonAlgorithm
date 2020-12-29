

# 首先是回文数，然后是素数，得出两个判定结果


class Solution():
    def primePalindrome(self, N: int) -> int:
        def isPrime(num):
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True if num > 1 else False
        
        def isPalindrome(num):
            return str(num) == str(num)[::-1]
        
        while True:
            if isPalindrome(N) and isPrime(N):
                return N
            else:
                if N > 11 and len(str(N)) % 2 == 0:
                    N = 10 ** len(str(N)) + 1
                else:
                    N += 1


if __name__ == "__main__":	
	s = Solution()
	print(s.primePalindrome(1000))     










