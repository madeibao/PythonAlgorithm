

class Solution:
    def __init__(self):
        self.c = 0
    def movingCount(self, m: int, n: int, k: int) -> int:
        hashDict = {}
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and (i,j) not in hashDict and self.count(i) + self.count(j) <= k:
                hashDict[(i,j)] = 1
                self.c += 1
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)

        dfs(0,0)
        return self.c

    def count(self,i):
        ans = 0
        while i:
            ans += i%10
            i //= 10
        return ans

if __name__ == "__main__":
    s = Solution()

    m = 2, n = 3, k = 1
    print(s.movingCount(m,n, k))