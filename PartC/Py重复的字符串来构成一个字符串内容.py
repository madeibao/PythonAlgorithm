


思路一：

该方法最容易想，就是找前缀，看s是否能有几个这样前缀组成。

思路二：

我们知道如果s是重复字符串，那么可以由两个子串组成。我们通过ss = s + s就有4个子串组成，

删除首尾字母，那么 ss[1:-1]就有应该有2个子串组成，就是说ss[1:-1]是否存在s

作者：powcai
链接：https://leetcode-cn.com/problems/repeated-substring-pattern/solution/bao-li-by-powcai-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s+s)[1:-1].find(s) != -1


if __name__ == "__main__":
    s = Solution()
    print(s.repeatedSubstringPattern("abcabc"))

    