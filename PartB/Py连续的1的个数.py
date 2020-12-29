



# 一个数组中的连续大的1的个数。
class Solution():
    def continuousNumber(self,nums):
        ans = 0
        count = 0
        for i in nums:
            if i==1:
                count += 1 
                ans = max(ans,count)
            else:
                count = 0
        return ans


if __name__=='__main__':
    s = Solution()
    print(s.continuousNumber([1,1,0,0,1,1,1]))









