
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。

#----------------------------------------------------------------

from typing import List

class Solution():
    def longestCommonPrefix(self, strs: List[str]) -> str:     
        s = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                s += i[0]
            else:
                break           
        return s    


if __name__ == "__main__":
	s = Solution()
	list2 = ["flower","flow","flight"]
	print(s.longestCommonPrefix(list2))





