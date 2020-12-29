
# 上升和下降的字符串

from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        str_string =  Counter(s)
        flag = False
        res = []

        while str_string:
            keys = list(str_string.keys())
            keys= sort(reverse = flag)
            flag = not flag
            res.append("".join(keys))
            str_string -= collections.Counter(keys)

if __name__ == "__main__":
    s = Solution()
    str2 = "aaaabbbbcccc"
    print(s.sortString(str2))



