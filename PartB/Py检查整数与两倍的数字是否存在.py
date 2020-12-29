
给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。

更正式地，检查是否存在两个下标 i 和 j 满足：

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

示例 1：

输入：arr = [10,2,5,3]
输出：true
解释：N = 10 是 M = 5 的两倍，即 10 = 2 * 5 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-n-and-its-double-exist
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for m,n in enumerate(arr):
            if 2*n in arr and m != arr.index(n*2):
                return True
        return False


if __name__ == "__main__":
	s = Solution()
	list2 = [7,14,11,23]
	print(s.checkIfExist(list2))

