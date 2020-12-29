

输入： "aaaba"
输出： 8
解释： 
只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。
"aaa" 出现 1 次。
"aa" 出现 2 次。
"a" 出现 4 次。
"b" 出现 1 次。
所以答案是 1 + 2 + 4 + 1 = 8。

#---------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------


import itertools

class Solution:
    def countLetters(self, S: str) -> int:
        res = 0
        for _, j in itertools.groupby(S):
            t = len(list(j))
            res += (1 + t)*t//2
        return res


if __name__ == "__main__":
	s = Solution()
	str2 ="aaaba"
	print(s.countLetters(str2))

