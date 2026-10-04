# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/4/星期日 21:58
# @File: selectword

from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        chars = [i for i in licensePlate if i.isalpha()]
        words = sorted(words, key=lambda x: len(x))

        for word in words:
            temp = chars.copy()
            for i in word:
                if i in temp:
                    temp.remove(i)
                if not temp:
                    return word
        return ""

if __name__ == '__main__':
    licensePlate = "1s3 456"
    words = ["looks", "pest", "stew", "show"]
    print(Solution().shortestCompletingWord(licensePlate, words))