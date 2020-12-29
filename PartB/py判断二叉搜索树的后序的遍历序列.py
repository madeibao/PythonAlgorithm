



from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def helper(nums):
            if len(nums)<1: return True
            root = nums[-1]
            i = 0
            for i_ in range(len(nums)-1):
                if nums[i_] > root: break
                i += 1
            print(i)
            for j in range(i, len(nums)-1):
                if nums[j] < root: return False
            return helper(nums[:i]) and helper(nums[i:-1])
        if not postorder: return True
        return helper(postorder)


if __name__ == "__main__":
    s = Solution()
    list2 =[1,3,2,6,8,7,5]
    print(s.verifyPostorder(list2))

