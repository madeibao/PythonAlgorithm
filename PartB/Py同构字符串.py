

给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

输入: s = "egg", t = "add"
输出: true

示例 2:
输入: s = "foo", t = "bar"
输出: false

示例 3:
输入: s = "paper", t = "title"
输出: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)): return False
        if len(set(zip(s, t))) == len(set(s)):
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic("add", "egg"))



