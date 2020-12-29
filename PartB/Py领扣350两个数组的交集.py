

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]



#---------------------------------------------------------------------------------------------------------------------------------
# ---------------	-------------------------	------------------	----------------	------------------	--------------------	----------------------
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        nums=[]
        for i in range(n):
            if nums1[i] in nums2:
                nums.append(nums1[i])
                nums2.remove(nums1[i])
        return nums



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = set(nums1) & set(nums2)
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i), nums2.count(i))
            l.extend([i] * min(nums1.count(i), nums2.count(i)))
        return l
