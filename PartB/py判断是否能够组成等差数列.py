

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        list2 = sorted(arr)
        for i in range(1, len(list2) - 1):
            if list2[i] - list2[i - 1] != list2[i + 1] - list2[i]:
                return False
        return True


if __name__ == "__main__":
	s =Solution()
	list2 = [3,5,1]
	print(s.canMakeArithmeticProgression(list2))

	