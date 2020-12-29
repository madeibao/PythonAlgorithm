
   '''
        关键是搞清楚格雷编码的生成过程, G(i) = i ^ (i/2);
        如 n = 3: 
        G(0) = 000, 
        G(1) = 1 ^ 0 = 001 ^ 000 = 001
        G(2) = 2 ^ 1 = 010 ^ 001 = 011 
        G(3) = 3 ^ 1 = 011 ^ 001 = 010
        G(4) = 4 ^ 2 = 100 ^ 010 = 110
        G(5) = 5 ^ 2 = 101 ^ 010 = 111
        G(6) = 6 ^ 3 = 110 ^ 011 = 101
        G(7) = 7 ^ 3 = 111 ^ 011 = 100
    '''


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

    

    