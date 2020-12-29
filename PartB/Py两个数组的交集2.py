

# # 求两个数组的交集，
# 给定两个数组，编写一个函数来计算它们的交集。

# 示例 1:

# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 示例 2:

# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 说明：

# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。

#================================================================

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = set(nums1) & set(nums2)
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i), nums2.count(i))  
        return l


if __name__ == "__main__":
    
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    s = Solution()
    print(s.intersect(nums1, nums2))

