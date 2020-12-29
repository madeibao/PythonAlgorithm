



from typing import List

# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]

# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # length1 = len(nums1)
        # length2 = len(nums2)
        #
        # minlength = min(length1, length2)
        #
        # list3 =[]
        # for i in range(minlength):
        #     if nums1[i] in nums2:
        #         list3.append(nums1[i])
        # return list3
        nums1.sort()
        nums2.sort()
        r = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                r.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return r


# nums1 = [1,2,2,1]
# nums2 = [2]

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]


nums1 = [1,2,2,1]
nums2 = [2,2]
cc = Solution()
print(cc.intersect(nums1, nums2))

