# 题目描述
# 小易在学校中学习了关于字符串的理论, 于是他基于此完成了一个字典的项目。
# 小易的这个字典很奇特, 字典内的每个单词都包含n个'a'和m个'z', 并且所有单词按照字典序排列。

# 小易现在希望你能帮他找出第k个单词是什么。

# 输入描述:
# 输入包括一行三个整数n, m, k(1 <= n, m <= 100, 1 <= k <= 109), 以空格分割。

# 输出描述:
# 输出第k个字典中的字符串，如果无解，输出-1。
# 示例1

# 示例1
# 输入
# 复制
# 2 2 6
# 输出
# 复制
# zzaa
# 说明
# 字典中的字符串依次为aazz azaz azza zaaz zaza zzaa

#================================================================

# 下面的算法时间复杂度过大。

import itertools


class Solution:
    def permute(self, nums):
        list2 = list(set(itertools.permutations(nums)))
        list3 = sorted(list2)
        return list3


if __name__ == '__main__':
    s = Solution()
    n, m, k = map(int, input().strip().split())
    str2 = str()
    str2 += 'a'*n
    str2 += 'z'*m
    list2 = list(str2)
    list3 = s.permute(list2)
    print(''.join(list3[k-1]))





# 方法2


def Cnm(a, b):
    ans = 1
    for i in range(a + 1, a + b + 1):
        ans *= i
    for i in range(1, b + 1):
        ans //= i
    return ans


n, m, k = map(int, input().strip().split())
if Cnm(n, m) < k:
    print(-1)
else:
    ans = ""
    while n > 0 and m > 0:
        temp = Cnm(n - 1, m)
        if temp < k:
            k -= temp
            ans += "z"
            m -= 1
        else:
            ans += "a"
            n -= 1
    ans += "a" * n
    ans += "z" * m
    print(ans)


























