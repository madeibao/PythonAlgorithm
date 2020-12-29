
while True:
    try:
        class Solution:
            def NumberOf1(self, n):
                count = 0
                # 负数与0xffffffff相与，消除死循环
                if n < 0:
                    n = n & 0xffffffff
                while n:
                    count += 1
                    # 把一个整数减去1，再和原整数做与运算，会把该整数最右边的一个1变成0
                    # 有多少个1就能进行多少次转化
                    n = n & (n - 1)
                return count

        if __name__ == '__main__':
            s = Solution()
            print(s.NumberOf1(-2))
    except:
        break

