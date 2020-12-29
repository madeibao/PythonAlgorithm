
# 删除其中的K个数字实现被删除后的数字为最小值。
题目：一个n位的数，去掉其中的k位，问怎样去掉使得留下来的那个（n-k）位的数最小？
分析：（删数问题，可用贪心算法求解），方法就是从简单入手，慢慢复杂。从n=1开始推导就会发现规律，
现在假设有一个数，124682385，
假如k = 1，则结果为12462385,k = 2，结果为1242385……
可以知道：最优解是删除出现的第一个左边>右边的数，因为删除之后高位减小，很容易想...那全局最优解也就是这个了，因为删除S个数字就相当于执行了S次删除一个数，因为留下的数总是当前最优解...


class Solution:
    """
    @param: A: A positive integer which has N digits, A is a string
    @param: l: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, K):
        A_list = list(A)
        flag = 0
        print(A_list)   # 此处也可以没有，仅仅是临时的打印的模块内容。
        # write your code here
        for _ in range(K):
            for i in range(flag, len(A_list) - 1):
                # 循环比较当前一位大于后一位的时候删除当前位，然后将下次遍历从删除位开始
                if int(A_list[i]) > int(A_list[i + 1]):
                    A_list.remove(A_list[i])
                    flag = i - 1 if i - 1 > 0 else 0
                    break
                # 有可能数组是不减的数组，所以在最后一次比较的时候也没有办法break这次循环，那么就直接删除最后一位即可，同样需要将下次循环以前一位开始
                elif i == len(A_list) - 2:
                    A_list.remove(A_list[-1])  # 删除的是最后的一位。
                    flag -= 1

        # 分成3种情况，因为首位为0必须将0删除，但是如果数组的长度只有1位那么就无需删除，如果最后数组的数据被全部删除，那么数组直接赋值为0
        if len(A_list) > 1:
            while A_list[0] == "0":
                A_list.remove("0")
        elif not A_list:
            A_list = ["0"]
        else:
            pass
        return "".join(A_list)


A = "1432219"
k = 3

cc = Solution()
print(cc.DeleteDigits(A, k))


# n = input().split(",")

# n0 = n[0]
# n1 = n[1]

# n0 = str(n0)
# print(n0)
# print(n1)