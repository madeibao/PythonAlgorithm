
# 给定一个字符串的内容，然后删除其中的重复性的元素，
# 并且要保持原来的重复的基本位置保持不变。

# 给出一个字符串，将重复的字符去除，仅保留第一次出现的字符，
# 且保持去重后的字符在原字符串中的顺序不变。
# 输入数据是一个字符串（不包含空格）
# 输出去重后的字符串
# 输入：12ere2
# 输出：12er


class Solution():
    def delDuplicate(self, str2):
        if len(str2) < 2:
            return str2
        result = []
        for i in str2:
            if i not in result:
                result.append(i)
        return ''.join(result)


if __name__ == '__main__':
    str2 = input()
    s = Solution()
    print(s.delDuplicate(str2))



# ==----------------------------------------------------------------
# 另一种方法来解决。

class Solution():
    def delDuplicate(self, str2):
        ss = list(set(str2))
        str3 = sorted(ss, key=str2.index)
        return "".join(str3)

if __name__ == '__main__':
    str2 = input()
    s = Solution()
    print(s.delDuplicate(str2))






                                          

