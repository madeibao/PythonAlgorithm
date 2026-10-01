

class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict2 = {}
        for i in s:
            dict2[i] = dict2.get(i,0)+1
        
        for k, v in enumerate(s):
            if dict2.get(v)==1:
                return k
        return -1

class Solution2:
    def firstUniqChar(self, s: str) -> int:
        res = len(s)
        for c in "abcdefghijklmnopqrstuvwxyz":
            left = s.find(c)
            if left != -1 and left == s.rfind(c):
                # find和rfind相等：说明只出现一次
                res = min(res, left)
        return res if res != len(s) else -1


if __name__=='__main__':
    s =Solution()
    list2= 'leetcode'
    print(s.firstUniqChar(list2))

    print(Solution2().firstUniqChar(list2))
