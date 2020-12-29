



class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n > 0:
            n -= 1
            s = chr(n%26+65) + s
            n =n//26
        return s


if __name__ == '__main__':
	s =Solution()
	num2= 28
	print(s.convertToTitle(num2))

	