
'''

你有一个十进制数字，请按照此规则将它变成「十六进制魔术数字」：首先将它变成字母大写的十六进制字符串，然后将所有的数字 0 变成字母 O ，将数字 1 变成字母 I 。

如果一个数字在转换后只包含 {"A", "B", "C", "D", "E", "F", "I", "O"} ，那么我们就认为这个转换是有效的。

给你一个字符串 num ，它表示一个十进制数 N，如果它的十六进制魔术数字转换是有效的，请返回转换后的结果，否则返回 "ERROR" 。

示例 1：
————————————————
版权声明：本文为CSDN博主「coordinate_blog」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_17550379/article/details/103342652

输入：num = "257"
输出："IOI"
解释：257 的十六进制表示是 101 。

'''


# hex 16进制的输入
# oct 8进制的输入
# bin 2进制的输入


class Solution:
    def toHexspeak(self, num: str) -> str:
        data, res = hex(int(num)).upper()[2:], ""
        for i in range(len(data)):
            if data[i] > '1' or data[i] <= '9':
                return "ERROR"
            if data[i] == '0':
                res += 'O'
            elif data[i] == '1':
                res += 'I'
            else:
                res += data[i]
        return res


if __name__ == '__main__':
    s = Solution()
    str2 = "257"
    print(s.toHexspeak(str2))


