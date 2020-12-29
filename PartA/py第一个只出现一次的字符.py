

# 如果是空字符串，则返回一个字符就可以了。

class Solution(object):
    def firstChar(self,strs):

        if not strs:
            return " "

        dict2 = {}

        for str in strs:
            dict2[str] = dict2.get(str,0) + 1

        for k, v in enumerate(strs):
            if dict2.get(v)==1:
                return v 
        return " "

if __name__ == "__main__":
    s = Solution()
    str = "leetcode"
    print(s.firstChar(str))

    

        