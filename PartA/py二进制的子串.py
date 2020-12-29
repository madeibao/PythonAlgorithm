


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        
        for i in range(N+1):
            if S.find(bin(i)[2:])==-1:
                return False
        return True

        

if __name__ == "__main__":
    s =Solution()
    s2 = "0110"
    N = 3
    print(s.queryString(s2, N))


