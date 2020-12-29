

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums) - 1):


        	# 非递减数列的对立面就是>

            if nums[i] > nums[i + 1]:
                if i == 0:
                    count += 1

                # 倒数第二个的位置
                elif i == len(nums) - 2:
                    count += 1
                else:
                    if nums[i + 2] >= nums[i]:
                        count += 1
                    elif nums[i - 1] <= nums[i + 1]:
                        count += 1
                    else:
                        return False

        # 如果出现的次数超过两次。
        if count >= 2:
            return False
        return True


if __name__ == "__main__":
	s = Solution()
	list2 = [4,2,3]
	print(s.checkPossibility(list2))




class Solution(object):
	def myShuzu(self,nums)
		n = len(nums)

		count = 0

		for i in range(n-1):

			# 非递减数列的对立的面就是递减数列。
			if nums[i]>nums[i+1]:
				if i==0:
					count += 1
				elif i==n-2:
					count += 1

				else:
					if nums[i+2]>=nums[i]:
						count += 1
					elif nums[i-1] <=nums[i+1]
						count += 1
					else:
						return False

		return False if count>=2 else True

if __name__ == "__main__":
	