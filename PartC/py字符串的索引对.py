

# 字符串的索引对子。


输入: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
输出: [[3,7],[9,13],[10,17]]

输入: text = "ababa", words = ["aba","ab"]
输出: [[0,1],[0,2],[2,3],[2,4]]
解释: 
注意，返回的配对可以有交叉，比如，"aba" 既在 [0,2] 中也在 [2,4] 中


from typing import List


class Solution:
    def indexPairs(self, text: str, words: 'List[str]') -> 'List[List[int]]':
        result = list()
        n = len(text)
        for word in words:
            begin = 0
            while text.find(word,begin) >= 0:
                idx = text.find(word,begin)
                result.append([idx,idx+len(word)-1])
                # 下一个开始的位置值。
                begin = idx + 1

        return sorted(result, key=lambda x:[x[0],x[1]])


if __name__ == '__main__':
    s = Solution()
    text = "ababa"
    words = ["aba", "ab"]
    print(s.indexPairs(text, words))





