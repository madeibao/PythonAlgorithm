
from typing import List
import collections


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ## 统计最大字母频率 ，然后比较.
        res = []
        dict_list = [collections.Counter(i) for i in B]
        print(dict_list)
        max_dict = {}
        for i in dict_list:
            for k, v in i.items():
                max_dict[k] = max(max_dict.get(k, 0), v)

        for a in A:
            a_count = collections.Counter(a)
            print(a_count)
            for k, v in max_dict.items():
                if v > a_count.get(k, 0):
                    break
            else:
                res.append(a)
        return res


if __name__ == "__main__":
    s = Solution()
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["lo", "eo"]
    print(s.wordSubsets(A,B))

