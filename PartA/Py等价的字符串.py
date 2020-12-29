

# 你将得到一个字符串数组 A。

# 如果经过任意次数的移动，S == T，那么两个字符串 S 和 T 是特殊等价的。

# 一次移动包括选择两个索引 i 和 j，且 i ％ 2 == j ％ 2，交换 S[j] 和 S [i]。

# 现在规定，A 中的特殊等价字符串组是 A 的非空子集 S，这样不在 S 中的任何字符串与 S 中的任何字符串都不是特殊等价的。

# 返回 A 中特殊等价字符串组的数量。

#  

# 示例 1：

# 输入：["a","b","c","a","c","c"]
# 输出：3
# 解释：3 组 ["a","a"]，["b"]，["c","c","c"]
# 示例 2：

# 输入：["aa","bb","ab","ba"]
# 输出：4
# 解释：4 组 ["aa"]，["bb"]，["ab"]，["ba"]
# 示例 3：

# 输入：["abc","acb","bac","bca","cab","cba"]
# 输出：3
# 解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]
# 示例 4：

# 输入：["abcd","cdab","adcb","cbad"]
# 输出：1
# 解释：1 组 ["abcd","cdab","adcb","cbad"]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/groups-of-special-equivalent-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


from typing import List
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
    	res = set()
    	for s in A:
    		res.add("".join(sorted(s[::2]))+"".join(sorted(s[1::2])))
    	return len(res)


if __name__ == "__main__":
	list2 = ["abc","acb","bac","bca","cab","cba"]
	s = Solution()
	print(s.numSpecialEquivGroups(list2))