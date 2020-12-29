



from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        s = [[len(x), set(x)] for x in words]
        res = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if not s[i][1] & s[j][1] and s[i][0]*s[j][0] > res:
                    res = s[i][0]*s[j][0]
        return res


if __name__ == "__main__":
    s = Solution()
    list2 = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    print(s.maxProduct(list2))

