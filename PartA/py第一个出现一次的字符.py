

class Solution:
    def firstUniqChar(self, s: str) -> str:

        dict2 = dict()
        for i in s:
            dict2[i] = dict2.get(i,0)+1
        for i, v in enumerate(s):
            if dict2.get(v)==1:
                return v   
        return " "


if __name__ == "__main__":
    s = Solution()
    str2 ="leetcode"
    print(s.firstUniqChar(str2))

        
        