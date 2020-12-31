
'''
class Solution(object):
    def isUgly(self, num):
        if num<1: return False

        # 自上而下的算法在顺序的执行。
        while num%5==0:
            num = num//5 
        while num%3 == 0:
            num = num//3    
        while num%2 == 0:
            num = num//2

        return num==1
'''

class Solution(object):
    def isUgly(self, num):
        if num<1: return False

        while True:
            if num==1:
                return True
            elif num%2==0:
                num = num//2
            elif num%3 == 0:
                num = num//3
            elif num%5 == 0:
                num = num//5
            else:
                return False
        return num==1


if __name__ == "__main__":
    s = Solution()
    num = 6
    print(s.isUgly(num))

