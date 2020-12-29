
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

# 示例 1:
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc" 

#-----------------------------------------------------------------------------------------

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list2 = [i for i in s.split()]

        return " ".join(i[::-1] for i in list2)


if __name__ == "__main__":
    s =Solution()
    print(s.reverseWords("Let's take LeetCode contest"))