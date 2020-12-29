
class Solution(object):
    def sort2(self, nums):
        i,j = 0, len(nums)-1

        while i<j:
            if nums[i]%2==1:
                i+=1
            elif nums[j]%2==0:
                j-=1
            else:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        return nums #

if __name__ == "__main__":
    s = Solution()  
    nums = [2,3,4,5]
    print(s.sort2(nums))
    


