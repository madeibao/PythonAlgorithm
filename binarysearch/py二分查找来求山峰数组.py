



## 一个山峰数组的索引的位置得值。


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low=0
        high=len(A)-1
        while low<high:
            mid=(low+high)//2
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                return mid
            elif A[mid]>A[mid-1]:
                low=mid+1
            else:
                high=mid


if __name__ == "__main__":
	s =Solution()
	list2 = [0,2,1,0]
	print(s.peakIndexInMountainArray(list2))


#-----------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------


class Solution(object):
	def peakIndexInMountainArray(self, nums):
		low = 0
		high = len(nums)-1

		while low < high:
			mid = (low+high)//2

			if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
				return mid 
			elif nums[mid] >nums[mid-1]:
				low = mid +1
			else:
				high = mid

if __name__ == "__main__":
	s =Solution()
	list2 = [0,2,1,0]
	print(s.peakIndexInMountainArray(list2))
		