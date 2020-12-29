
class Solution(object):
    def multiply(self,nums):

        b = [1]*len(nums)
        temp = 1

        for i in range(1, len(nums)):
            b[i] = b[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            temp *= nums[i+1]
            b[i] *= temp
        return b


if __name__ == "__main__":
    s = Solution()
    a = [1,2,3,4]
    print(s.multiply(a))    