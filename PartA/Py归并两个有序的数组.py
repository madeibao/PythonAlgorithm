
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List:

        nums1[m:m+n] = nums2
        nums1.sort()
        return nums1

if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    res = s.merge(nums1,m,nums2,n)
    print(res)
    