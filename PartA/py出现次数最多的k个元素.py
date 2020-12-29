



class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = dict()
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

        output = sorted(m.items(), key=lambda e: e[1], reverse=True)

        final = []
        for i in range(k):
            final.append(output[i][0])
        return final

if __name__ == "__main__":
	s = Solution()
	nums = [1,1,1,2,2,3]
	k = 2
	print(s.topKFrequent(nums, k))


