

class Solution:
    def trailingZeroes(self, n: int) -> int:
        result=0
        n_fake=n
        while n_fake>=5:
            n_fake/=5
            result+=int(n_fake)
        return result


if 	__name__ == "__main__":
	s =Solution()
	print(s.trailingZeroes(9))