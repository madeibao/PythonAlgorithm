给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，
该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
若无答案，则返回空字符串。
示例 1:

输入: 
words = ["w","wo","wor","worl", "world"]
输出: "world"
解释: 
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。

示例 2:

输入: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出: "apple"
解释: 
"apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。

#----------------------------------------------------------------------------------------

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        dict = [[] for _ in range(31)]

        for word in words:
            dict[len(word)].append(word)
        longestword = set(dict[1])

        for i in range(2, 31):
            tmp = [w for w in dict[i] if w[:-1] in longestword]
            if not tmp:
                break
            longestword = tmp

        return sorted(longestword)[0]


if __name__ == '__main__':
    s = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(s.longestWord(words))

