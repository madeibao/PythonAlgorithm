


import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,j in collections.Counter(s).items():
            if j==1:return s.index(i)
        return -1

if __name__=='__main__':
    s =Solution()
    str2 = "leetcode"
    print(s.firstUniqChar(str2))

    