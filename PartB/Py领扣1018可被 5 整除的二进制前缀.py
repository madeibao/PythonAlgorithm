# 输入：[0,1,1]
# 输出：[true,false,false]
# # 解释：
# # 输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
# 给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。
# 返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。

# 下面的这种办法会超时。

from typing import List
import functools

#===============================================================================
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        b = []
        c = []
        d = []
        e = []
        for i in range(len(A)):
            a = A[:i+1]
            b.append(a)
        for list1 in b:
            str2 = "0b"+"".join(str(i) for i in list1)
            c.append(str2)
        for j in c:
            m = int(j, 2)
            d.append(m)

        for k in d:
            if k % 5 == 0:
                e.append(True)
            else:
                e.append(False)
        return e


#============================================================================
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        temp = 0
        for num in A:
            temp = temp * 2 + num
            result.append(temp % 5 == 0)
        return result



if __name__ == '__main__':
    s = Solution()
    print(s.prefixesDivBy5([1, 1, 1]))

