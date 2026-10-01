

from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            max_gift = max(gifts)
            gifts[gifts.index(max_gift)] = int(max_gift ** 0.5)
            k -= 1
        return sum(gifts)

if __name__ == "__main__":
    gifts = [25, 64, 9, 4, 100]
    k = 4
    print(Solution().pickGifts(gifts, k))

