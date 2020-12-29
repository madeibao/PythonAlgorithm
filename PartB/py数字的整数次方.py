

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n < 0:
            x = 1/x
            n = -n


        # 注意的是python中整数的形式 //  
        mid = self.myPow(x,n//2)
        if n%2==1:
            return mid*mid*x
        else:
            return mid*mid


if __name__ == "__main__":
    s = Solution()
    x = 10.0
    n = 2
    print(s.myPow(x,n))


        

