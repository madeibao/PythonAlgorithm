








from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict = {i: i for i in nums if i > 0}
        n = len(dict)
        for i in range(1, n + 1):
            if i not in dict:
                return i
        return n + 1


if __name__ == "__main__":
    s = Solution()
    list2 = [1, 2]
    print(s.firstMissingPositive(list2))
