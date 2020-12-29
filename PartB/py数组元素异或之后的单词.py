


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        c=[]
        res=0
        for i in range(n):
            c.append(start+2*i)
            res = res^c[i]
        return res


if __name__ == "__main__":
	s =Solution()
	n = 5
	start = 0

	print(s.xorOperation(n, start))

	