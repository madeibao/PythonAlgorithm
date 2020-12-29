
from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j  = 0, len(nums)-1
        while i < j:
            if nums[i]%2==1:
                i+=1
            elif nums[j]%2==0:
                j-=1
            else:
                nums[i], nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        return nums


if __name__ == "__main__":
    s =Solution()
    list2 = [2,3,4,5]
    print(s.exchange(list2))

    