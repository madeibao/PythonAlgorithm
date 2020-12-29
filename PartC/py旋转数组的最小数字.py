

class Solution(object):
    def rotate(self,nums):
        i,j = 0,len(nums)-1

        while i<j:
            mid = (i+j)//2
            if nums[mid]>nums[j]:
                i =mid+1
            elif nums[mid]<nums[j]:
                j = mid
            else:
                j = j-1
        return nums[i]


if __name__ == "__main__":
    s= Solution()
    nums = [3,4,5,6,1,2]
    print(s.rotate(nums))