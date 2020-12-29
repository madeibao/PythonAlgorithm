
# 给定数组，然后给出数组中的最大的数的索引，单调增，然后单调减少。


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = (low + high) // 2
            if   A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid - 1] < A[mid] and A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1


if __name__ == "__main__":
    s = Solution()
    print(s.peakIndexInMountainArray([1,2,1]))




