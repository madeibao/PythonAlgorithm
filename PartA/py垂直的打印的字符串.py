
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:

        s = s.split()
        res = []
        num2 = max(len(x) for x in s)

        for i in s:
            res.append(i.ljust(num2))

        res2 = []
        for i in zip(*res):
            res2.append("".join(i).rstrip(" "))
        return res2


if __name__ == "__main__":
    s = Solution()
    s2 = "TO BE OR NOT TO BE"
    print(s.printVertically(s2))








class Solution:
    def printVertically(self, s: str) -> List[str]:
        s1=list(s.split())
        maxLen=0
        ret=[]
        for i in range(len(s1)):
            maxLen=max(maxLen,len(s1[i]))
        for i in range(len(s1)):
            s1[i]=s1[i].ljust(maxLen)
        for i in range(maxLen):
            temp="".join([sp[i] for sp in s1])
            temp=temp.rstrip()
            ret.append(temp)
        return ret

