


from typing import List
import collections
import bisect


# 字典的拖地案件的排序。
# 智商安在地板上摩擦
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        return sorted(c, key=lambda s: (-c[s], s))[: k]


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        q = []
        for i, s in enumerate(c):
            bisect.insort_left(q, (-c[s], s), hi = min(i, k))
        return [s for _,  s in q[: k]]



class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        q = []
        for i, s in enumerate(c):
            bisect.insort_left(q, (-c[s], s))
            if i >= k:
                q.pop()
        return [s for _,  s in q[: k]]


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        return heapq.nsmallest(k, c, lambda s: (-c[s], s))


# 字典的多条件的排序来实现前面的高频个k个单词的排序。


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = sorted([(v,c) for c,v in Counter(words).items()], key = lambda x: (-x[0], x[1]))
        return [cnt[i][1] for i in range(k)]

#-----------------------------------------------------------------------------------------------------------------



if __name__=="__main__":
    str2 = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    s =Solutin()
    print(s.topKFrequent(str2, k))

