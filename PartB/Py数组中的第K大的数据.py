在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。



import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    s = Solution()
    num2 = [3,2,1,5,6,4]
    k = 2
    print(s.findKthLargest(num2, k))


