'''
输入：
["a","a","b","b","c","c","c"]

输出：
返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]

说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。

输入：
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

输出：
返回4，输入数组的前4个字符应该是：["a","b","1","2"]。

说明：
由于字符"a"不重复，所以不会被压缩。"bbbbbbbbbbbb"被“b12”替代。
注意每个数字在数组中都有它自己的位置。
'''


from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 0                             # 计数器cnt用于一次计数过程中，连续出现变量l中字符的个数
        pointer = 0                         # pointer是下一次写入chars数组字符时的位置
        if len(chars) == 1:                 # 如果chars数组元素只有一个
            return len(chars)               # 那么，直接返回chars长度，无需修改
        else:                               # 如果chars数组元素个数大于1
            for i in range(len(chars)):     # 遍历循环数组chars
                l = chars[i]                # 将滑窗左侧的字符赋值l
                r = chars[i + 1] if i < len(chars) - 1 else None    # 将滑窗右侧的字符赋值r，如果数组越界则赋值None
                if l == r:                  # 如果l==r，则计数+1
                    cnt += 1
                else:                       # 如果遇到l!=r，则停止计数
                    chars[pointer] = l      # 将字符l写进pointer所在的位置
                    pointer += 1            # 写入后，更新pointer，pointer自加1
                    if cnt != 0:            # 如果有连续的字符，则还需在此字符后面写入该字符的数量
                        for idx, val in enumerate(list(str(cnt + 1))):
                            chars[pointer] = val
                            pointer += 1    # 每写一次chars数组，更新一次位置
                    cnt = 0                 # 一次计数结束后，cnt置0  每一次的计数完成之后，都要清空。
        for i in range(pointer, len(chars)): # 将多余的数据删除
            chars.pop(-1)
        return len(chars)


if __name__ == '__main__':
    s = Solution()
    print(s.compress["a","a","b","b","c","c","c"])



#===========================================================================================================
#================================================================================================

题目描述
对字符串进行RLE压缩，将相邻的相同字符，用计数值和字符值来代替。例如：aaabccccccddeee，则可用3a1b6c2d3e来代替。

输入描述:
输入为a-z,A-Z的字符串，且字符串不为空，如aaabccccccddeee
输出描述:
压缩后的字符串，如3a1b6c2d3e

# 字符串的压缩


import sys

if __name__ == "__main__":
    # sys.stdin = open("input.txt", "r")
    s = input().strip()
    count = 1
    ans = ""
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            ans += str(count) + s[i - 1]
            count = 1
    ans += str(count) + s[-1]
    print(ans)
