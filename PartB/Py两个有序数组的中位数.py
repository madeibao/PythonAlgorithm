
# nums1 = [-1,1,3,5,7,9]
# nums2 = [2,4,6,8,10,12,14,16]


思路：
这道题如果时间复杂度没有限定在 O(log(m+n))O(log(m+n))O(log(m+n))，我们可以用 O(m+n)O(m+n)O(m+n) 的算法解决，用两个指针分别指向两个数组，比较指针下的元素大小，一共移动次数为 (m+n + 1)/2，便是中位数。
首先，我们理解什么中位数：指的是该数左右个数相等。
比如：odd : [1,|  2  |,3]，2 就是这个数组的中位数，左右两边都只要 1 位；
even: [1,|  2, 3  |,4]，2,3 就是这个数组的中位数，左右两边 1 位；
那么，现在我们有两个数组：
num1: [a1,a2,a3,...an]
nums2: [b1,b2,b3,...bn]
[nums1[:left1],nums2[:left2]  |  nums1[left1:], nums2[left2:]]
只要保证左右两边 个数 相同，中位数就在 | 这个边界旁边产生。
如何找边界值，我们可以用二分法，我们先确定 num1 取 m1 个数的左半边，那么 num2 取 m2 = (m+n+1)/2 - m1 的左半边，找到合适的 m1，就用二分法找。
当 [  [a1],[b1,b2,b3]    |  [a2,..an],[b4,...bn]    ]
我们只需要比较 b3 和 a2 的关系的大小，就可以知道这种分法是不是准确的！
例如：我们令：
nums1 = [-1,1,3,5,7,9]
nums2  =[2,4,6,8,10,12,14,16]
当 m1 = 4,m2 = 3 ,它的中位数就是median = (num1[m1] + num2[m2])/2
时间复杂度：O(log(min(m,n)))O(log(min(m,n)))O(log(min(m,n)))
对于代码中边界情况，大家需要自己琢磨。


#==============================================================================
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:    # 默认的是第一个列表比较短.
            return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1)//2
        left = 0
        right = n1
        while left < right:
            m1 = left + (right - left)//2
            m2 = k - m1
            # nums1 = [-1,1,3,5,7,9]
            # nums2 = [2,4,6,8,10,12,14,16]
            # print(m1)
            # print(m2)
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1

        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"), nums2[m2-1] if m2 > 0 else float("-inf"))
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        return (c1 + c2) / 2


if __name__ == '__main__':
    s = Solution()
    nums1 = [-1, 1, 3, 5, 7, 9]
    nums2 =[2, 4, 6, 8, 10, 12, 14, 16]
    print(s.findMedianSortedArrays(nums1, nums2))








