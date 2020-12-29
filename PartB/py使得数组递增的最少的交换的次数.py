
'''

4
2 1 3 4 
则只需要 2 和 1 交换一次就能变成递增的方式。

'''




from typing import List


class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n, f1, f2 = len(A), 0, 1
        for i in range(1, n):
            s1 = A[i - 1] < A[i] and B[i - 1] < B[i]
            s2 = A[i - 1] < B[i] and B[i - 1] < A[i]
            if s1 and s2:
                f1, f2 = min(f1, f2), min(f1, f2) + 1
            elif s1:
                f2 += 1
            else:
                f1, f2 = f2, f1 + 1
        return min(f1, f2)


if __name__ == "__main__":
    s = Solution()
    num = int(input())
    list2 = list(map(int, input().split(" ")))
    list3 = sorted(list2)
    print(s.minSwap(list2,list3))
