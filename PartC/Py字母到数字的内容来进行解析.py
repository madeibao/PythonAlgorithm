# 给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：

# 字符（'a' - 'i'）分别用（'1' - '9'）表示。
# 字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
# 返回映射之后形成的新字符串。

# 题目数据保证映射始终唯一。

#  

# 示例 1：

# 输入：s = "10#11#12"
# 输出："jkab"
# 解释："j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 返回的结果也用字符串的形式来进行表示。

# class Solution():
#     def freqAlphabets(self, s: str) -> str:
#         def get(st):
#             return chr(int(st) + 96)

#         i, ans = 0, ""
#         while i < len(s):
#             if i + 2 < len(s) and s[i + 2] == '#':
#                 ans += get(s[i : i + 2])
#                 i += 2
#             else:
#                 ans += get(s[i])
#             i += 1
#         return ans

# 字母a的ascii码的值为97


class Solution():
    def freqAlphabets(self, s: str) -> str:

        def get(st):
            return chr(int(st)+96)   # a的ascii码的值为97.

        i,ans = 0,""
        while i <len(s):
            if i+2<len(s) and s[i+2] == '#':
                ans += get(s[i:i+2])
                i += 2
            else:
                ans += get(s[i])
            i+=1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.freqAlphabets("10#11#12"))













