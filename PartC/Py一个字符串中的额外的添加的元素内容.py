



import collections

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(collections.Counter(t) - collections.Counter(s))[0]


if __name__ == "__main__":
    s  = Solution()
    print(s.findTheDifference("abcd", "abcde"))


# # 方法2的内容。 变成了只是出现一次的数字。

# class Solution():
#     def findTheDifference(self, s: str, t: str) -> str:
#         tmp = s + t
#         res = ord(tmp[0])
#         for t in tmp[1:]:
#             res ^= ord(t)
#         return chr(res)


# if __name__ == "__main__":
#     s = Solution()  
#     print(s.findTheDifference("abcd","abcde"))



