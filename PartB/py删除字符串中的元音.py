


# class Solution:
#     def removeVowels(self, S: str) -> str:
#         res=''
#         a={'a','e','i','o','u'}
#         for i in S:
#             if i not in a:
#                 res+=i
#         return res

class Solution:
    def removeVowels(self, S: str) -> str:
        res="aeiou"
        return "".join(list(filter(lambda x:x not in res,S)))


if __name__ == '__main__':
    s =Solution()
    str2 = "leetcodeisacommunityforcoders"
    print(s.removeVowels(str2))
