

# 两个数字的平方和的结果值。

class Solution:
    def powTwo(self,num):
        i,j = 0, int(num**0.5)

        while i<=j:
            temp = i*i+j*j
            if temp==num: 
                return True
            elif temp>num:
                j-=1
            else:
                i+=1
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.powTwo(5))