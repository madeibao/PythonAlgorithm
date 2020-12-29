

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        res = list()
        for i in range(1 << n):
            res.append(i ^ (i>>1))
        return res


if __name__ == "__main__":
    s = Solution()  
    n = 3
    print(s.grayCode(n))

    

    