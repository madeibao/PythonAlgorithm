


class Solution():
    def distance(self,n):
        if n==0:
            return 0
        return n+n//2+self.distance(n//2)

if __name__ == "__main__":
    s = Solution()
    print(int(s.distance(100)))

