


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            if not res or sorted(word) != sorted(res[-1]):
                res.append(word)
        return res

if __name__ == '__main__':
    print(Solution().removeAnagrams(["abba","baba","bbaa","cd","cd"]))

    