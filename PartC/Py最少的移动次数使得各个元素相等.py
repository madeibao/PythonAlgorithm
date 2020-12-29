



class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length=len(nums)
        target=0
        if length%2==1:
            pos=length//2+1
        else:
            pos=length//2
        target=nums[pos-1]
        count=0
        for i in range(pos-1):
            count+=target-nums[i]
        for i in range(pos,length):
            count+=nums[i]-target
        return count


if __name__ == "__main__":
	list2 = [1, 2, 3,]
	s = Solution()
	print(s.minMoves2(list2))

