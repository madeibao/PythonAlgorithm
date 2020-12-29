
from typing import List


class Solution:
    def longestWord(self, words) -> str:
        words.sort()
        # print(words)
        save = set()
        res = ""
        for word in words:
            # 如果单词通过集合中的单词扩展而来，或者单词只有一个字母
            if word[:-1] in save or word[:-1] == '':
                if len(word) > len(res):        # 遇到更长的单词
                    res = word                  # 更新结果
                save.add(word)                  # 添加到单词表
        return res


if __name__ == "__main__":
    s =Solution()
    list2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(s.longestWord(list2))


