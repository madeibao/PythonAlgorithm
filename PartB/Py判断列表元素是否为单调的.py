


class Solution:
    def isMonotonic(self, A) -> bool:
        B = sorted(A)
        C = sorted(A, reverse=True)
        if A == B or A == C:
            return True
        else:
            return False


num = [1, 2, 3, 4, 5, 8, 7]
cc = Solution()
print(cc.isMonotonic(num))




# 判断一个列表的内容是否为严格的单调递增或者是严格的单调递减，没有重复的元素

例如[1,2,3,4,5,6,7]  是严格的单调递
[1,2,2,3,3,] 这种就不是严格的单调递，有重复的元素内容存在。



class Solution:
    def isMonotonic(self, A) -> bool:
        if sorted(A) == A and len(set(A)) == len(A):
            return True
        elif sorted(A) == A[::-1] and len(set(A)) == len(A):
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isMonotonic([3, 2, 1]))





