

class Solution(object):
    def isPowerOfFour(self,num):
        if num<0 or (num&(num-1)):return False
        return (num-1)%3==0

if __name__ == "__main__":
    s = Solution()
    num = 16
    print(s.isPowerOfFour(num))

    