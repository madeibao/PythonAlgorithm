

class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict2 = {}
        for i in s:
            dict2[i] = dict2.get(i,0)+1
        
        for k, v in enumerate(s):
            if dict2.get(v)==1:
                return k
        return -1


if __name__=='__main__':
    s =Solution()
    list2= 'leetcode'
    print(s.firstUniqChar(list2))

