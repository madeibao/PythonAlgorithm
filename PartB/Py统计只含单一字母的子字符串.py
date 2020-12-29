

输入： "aaaba"
输出： 8
解释： 
只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。
"aaa" 出现 1 次。
"aa" 出现 2 次。
"a" 出现 4 次。
"b" 出现 1 次。
所以答案是 1 + 2 + 4 + 1 = 8。
第二种思路：

按照数学的方法，先找出由单一字母构成的连续子串的长度N，

然后（N + 1） * N 就是这一个子串的答案的数量。

比如 "aaaba"，可以分成 "aaa" "b" "a"， 
"aaa" 可以构成满足题目要求的子串 "aaa", "aa", "aa", "a", "a", "a", 答案数相当于从 1 + 2 + ... + N。

#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

import itertools


class Solution:
    def countLetters(self, S: str) -> int:
        res = 0
        for _, j in itertools.groupby(S):
            t = len(list(j))
            # 等差数列的求和公式
            res += (1 + t)*t//2
        return res


if __name__ == "__main__":
    s  = Solution()
    print(s.countLetters("aaaba"))



#-----------------------------------------------------------------------------

class Solution():
    def countLetters(self, S: str) -> int:
        # 连续长度为n的相同元素的单个字符子串个数为：n(n+1) / 2
        # 统计连续出现的个数
        total = 0
        n = 1
        S = S + '#' # 添加一个哨兵结点
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                n += 1
            else:
                total += n * (n + 1) // 2
                n = 1
        return total  


if __name__ == "__main__":
    s = Solution()  
    print(s.countLetters("aaaaaa"))


