
from typing import List


class Solution():
    def findWords(self, words: List[str]) -> List[str]:
        set1, set2, set3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        ans = []
        for i in words:
            t = set(i.lower())
            # 利用集合来进行判断内容。
            if t <= set1 or t <= set2 or t <= set3:
                ans.append(i)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))


#----------------------------------------------------------------
# 方法二的内容，求两个数字的交集，来是新。
class Solution(object):
    def findWords(self,words):
        l1 = 'qwertyuiopQWERTYUIOP'
        l2 = 'asdfghjklASDFGHJKL'
        l3 = 'zxcvbnmZXCVBNM'

        l1,l2,l3 =set(l1),set(l2),set(l3)
        final = []

        for i in range(len(words)):
            s =set(words[i])
            if s&l1== s or s&l2== s or s&l3== s:
                final.append(words[i])
        return final



if __name__ == "__main__":
    s = Solution()
    print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))
