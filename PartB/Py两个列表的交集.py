

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
	s = Solution()
	list2 = [1,2,2,1]
	list3 = [2,2]
	print(s.intersect(list2,list3))





