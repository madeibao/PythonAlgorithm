# 字母的移位词语分组单词。
from typing import List


class Solution(object):
    def group(self, strs:List[str]) -> List[List[str]]:
        dict2 = {}
        for i in strs:
            temp = "".join(sorted(list(i)))
            if temp in dict2:
                dict2[temp].append(i)
            else:
                dict2[temp] = [i]
        return list(dict2.values())


if __name__ == "__main__":
    s = Solution()
    list2 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.group(list2))
