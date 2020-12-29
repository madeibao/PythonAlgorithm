

# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。

# 示例 1:

# 输入: "A man, a plan, a canal: Panama"
# 输出: true


# 示例 2:

# 输入: "race a car"
# 输出: false

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         i, j = 0, len(s) - 1
#         while i < j:
#             while i < len(s) and not s[i].isalnum():
#                 i += 1
#             while j > -1 and not s[j].isalnum():
#                 j -= 1
#             if i > j:
#                 return True
#             if s[i].upper() != s[j].upper():
#                 return False
#             else:
#                 i += 1
#                 j -= 1
#         return True


# ------------------------------
#-----------------------------------------------------------------------------

# 自己定义的方法内容


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = s.replace(" ", "").lower()  # 去除空格，统一的转化为小写字母的形式。
        list2 = []
        for i in range(len(s2)):
            if (ord(s2[i])>= 97 and ord(s2[i]) <= 122) or (ord(s2[i])<= 57 and ord(s2[i])>= 48) or (ord(s2[i])>=65 and ord(s2[i])<=90):
                list2.append(s2[i])

        if list2[::-1] == list2:
            return True
        else:
            return False


if __name__ == '__main__':
    s1 = "A man, a plan, a canal: Panama"
    s= Solution()
    print(s.isPalindrome(s1))
