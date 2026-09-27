

from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        res = {}
        for i in words:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        sorted_res = sorted(res.items(), key=lambda x: (-x[1], x[0]))
        return [i[0] for i in sorted_res[:k]]


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(Solution().topKFrequent(words, k))