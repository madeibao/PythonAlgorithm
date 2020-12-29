


import string

from typing import List
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return []
        res = ['']
        for i in S:
            temp = []
            for j in res:
                if i in string.ascii_letters:
                    temp.append(j + i.upper())
                    temp.append(j + i.lower())
                else:
                    temp.append(j + i)
            res = temp
        return res


#================================================================
# 方法2的内容
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = list()
        # 字符串的长度。
        l = len(S)
        if l == 0:
            return [""]
            
        def dfs(start, temp):
            if start >= l or len(temp) == l: #已经找到了一个答案
                res.append(temp)
                return
            # print start, temp
            if S[start].isdigit(): #数字就直接加
                dfs(start + 1, temp + S[start])
            
            elif S[start].islower(): #字母就加本身和对立面
                dfs(start + 1, temp + S[start])
                dfs(start + 1, temp + S[start].upper())

            elif S[start].isupper():
                dfs(start + 1, temp + S[start])
                dfs(start + 1, temp + S[start].lower())
        
        dfs(0, "")
        return res




if __name__ == '__main__':
    s = Solution()
    print(s.letterCasePermutation("a1b2"))


