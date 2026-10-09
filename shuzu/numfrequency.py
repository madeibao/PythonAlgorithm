
from typing import List
from collections import Counter

class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        minaveloru = nums  # 按题意保存输入
        counter = Counter(minaveloru)
        freq_count = Counter(counter.values())

        for num in minaveloru:
            if freq_count[counter[num]] == 1:
                return num
        return -1


if __name__ == "__main__":
    nums = [20,20,10,30,30,30]
    print(Solution().firstUniqueFreq(nums))
