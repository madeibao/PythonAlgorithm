

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d={}
        for ix,num in enumerate(nums):
            if num not in d:
                d[num]=ix

            # 如果已经存在了这个元素的话，就字典的操作。
            else:
                if ix-d[num]<=k:
                    return True
                else:
                    d[num]=ix
        return False


if __name__ == "__main__":
	s = Solution()
	nums = [1,2,3,1]
	k = 3
	print(s.containsNearbyDuplicate(nums, k))





