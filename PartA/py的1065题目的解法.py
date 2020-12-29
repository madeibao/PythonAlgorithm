


# 给出 字符串 text 和 字符串列表 words, 
# 返回所有的索引对 [i, j] 使得在索引对范围内的子字符串 text[i]...text[j]
# （包括 i 和 j）
# 属于字符串列表 words


# 输入: text = “thestoryofleetcodeandme”, words = [“story”,“fleet”,“leetcode”]
# 输出: [[3,7],[9,13],[10,17]]

# 输入: text = “ababa”, words = [“aba”,“ab”]
# 输出: [[0,1],[0,2],[2,3],[2,4]]
# 解释: 注意，返回的配对可以有交叉，比如，“aba” 既在 [0,2] 中也在 [2,4] 中

#--------------------------------------------------------------------------------------------------


from typing import List, Tuple


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        st = set(words)
        n = len(text)
        for i in range(n):
            for j in range(i + 1, n + 1):
                tt = text[i: j]
                if not tt in st:
                    continue
                res.append([i, j - 1])
        return res


if __name__ == "__main__":
    s = Solution()
    text = "ababa"
    words = ["aba","ab"]
    print(s.indexPairs(text, words))
