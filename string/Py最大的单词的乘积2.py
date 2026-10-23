from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 位掩码：用一个整数的 26 个二进制位标记单词出现了哪些字母
        # 第 k 位为 1 <=> 字母 chr(ord('a') + k) 出现过
        # 相同字符集的单词只保留最长长度（乘积只取决于长度）
        best = {}  # mask -> 该字符集下的最大单词长度
        for w in words:
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - ord('a'))
            if len(w) > best.get(mask, 0):
                best[mask] = len(w)

        res = 0
        items = list(best.items())
        for i in range(len(items) - 1):
            mask_i, len_i = items[i]
            for j in range(i + 1, len(items)):
                mask_j, len_j = items[j]
                # 按位与为 0 <=> 两个单词的字符集不相交
                if mask_i & mask_j == 0:
                    res = max(res, len_i * len_j)
        return res

if __name__ == "__main__":
    s = Solution()
    cases = [
        ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],  # 期望 16: "abcw" x "xtfn"
        ["a", "ab", "abc", "d", "cd", "bcd", "abcd"],      # 期望 4:  "ab" x "cd"
        ["a", "aa", "aaa", "aaaa"],                        # 期望 0:  全都含 'a'
    ]
    for words in cases:
        print(f"{words} -> {s.maxProduct(words)}")
