

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1=[]
        for i in range(len(nums)-1):
            if i%2==0:
                for _ in range(nums[i]):
                    nums1.append(nums[i+1])
        return nums1



if __name__ == "__main__":
	s =Solution()
	print(s.decompressRLElist([1,1,2,3]))

