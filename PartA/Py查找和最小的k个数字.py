

from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    	if not nums1 or not nums2:
    		return [[]]
    	res = []
    	for i in nums1:
    		for j in nums2:
    			res.append([i,j])

    	res.sort(key = sum)

    	return res[:k]

if __name__ == "__main__":
	s =  Solution()

	nums1 = [1,7,11]
	nums2 = [2,4,6]
	k = 3

	print(s.kSmallestPairs(nums1, nums2, k))

