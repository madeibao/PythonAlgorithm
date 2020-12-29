


给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。
如果剩余少于 k 个字符，则将剩余的所有全部反转。
如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
示例:


输入: s = "abcdefg", k = 2
输出: "bacdfeg"


#----------------------------------------------------------------
#----------------------------------------------------------------

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list2 = []
        for i in range(0, len(s), k):
            list2.append(s[i:i+k])
        list3 = []
        for i in range(0, len(list2)):
            if i % 2 == 0:
                list3.append(list2[i][::-1])
            else:
                list3.append(list2[i])

        return "".join(list3)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefghijklmn", 2))






