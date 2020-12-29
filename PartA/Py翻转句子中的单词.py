
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#================================================================
#============================================================================


class Solution:
    def reverseWords(self, s: str) -> str:
    	list2 = s.split(" ")
    	print(list2)
    	res = ""
    	temp = " "
    	for i in list2:
    		res += i[::-1]
    		res += temp
    	return res.rstrip()

if __name__ == "__main__": 
	s = Solution()
	nums = "Let's take LeetCode contest"
	print(s.reverseWords(nums))


# ============================== 
# 方法2的结果。

class Solution:
    def reverseWords(self, s: str) -> str:
    	return ' '.join(i[::-1] for i in s.split(" "))

