

给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。
示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]


示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]

#============================================================================

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res=[]
        if not A:
            return res
        key = set(A[0])  # 给出一个集合的内容。
        for k in key:
            minnum = min(a.count(k) for a in A)
            res.extend(minnum*k)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(["cool", "lock", "cook"]))




