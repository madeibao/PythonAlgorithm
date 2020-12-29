from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(-n + 1, n, 2))

if __name__ == "__main__":
    s = Solution()
    print(s.sumZero(5))




