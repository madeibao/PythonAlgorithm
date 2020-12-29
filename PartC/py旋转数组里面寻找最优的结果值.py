

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            if nums[i]<=nums[mid]:
                if nums[i]<=target<nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
            else:
                if nums[mid]<target<=nums[j]:
                    i=mid+1
                else:
                    j=mid-1
        return -1


class Solution():
    def search(self,nums, target):
        if not nums:
            return -1

        l = 0
        h = len(nums)-1

        while l<h:
            mid = (i+j)//2

            if nums[mid]==target
                return mid
            if nums[l]<=nums[mid]:
                if nums[l] <=target<=nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<target<nums[h]:
                    i = mid +1
                else:
                    j = mid- 1

        return -1
        

if __name__ == "__main__":
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(s.search(nums, target))






