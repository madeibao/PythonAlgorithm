# 有N个人参加比赛，每个人比赛结束后都会得到一个分数，现在将N个人排成一圈领取奖品，要求：
# 如果某个人的分数比左右的人稿，那么奖品数字一定要比左右人的多。
# 每个人至少得到一个奖品。
# 问最少应该准备多少奖品？
# 解：左右遍历，判断奖品数。需要注意的一点是：**N个人围成一个圈。**所以首尾需要判断。

# 题目的原型：LeetCode135——分发糖果
# 2019年3月16日字节跳动的编程算法实习岗位题目



class Solution:
    def minnum(self, data):
        n = len(data)
        m = min(data)
        loc = data.index(m)
        res = 0
        # 初始化奖品数，保证每个人都有一个奖品
        num1 = [1 for i in range(n)]
        num2 = [1 for i in range(n)]
        # 向右遍历
        for i in range(loc + 1, n):
            if data[i] > data[i - 1]:
                num1[i] = num1[i - 1] + 1
        if data[0] > data[n - 1]:
            num1[0] = num1[i]
        for i in range(1, loc):
            if data[i] > data[i - 1]:
                num1[i] = num1[i - 1] + 1


        # 向左遍历
        for j in range(loc, 0, -1):
            if data[j - 1] > data[j]:
                num2[j - 1] = num2[j] + 1
        if data[n - 1] > data[0]:
            num2[n - 1] = num2[0] + 1
        for j in range(n - 1, loc, -1):
            if data[j - 1] > data[j]:
                num2[j - 1] = num2[j]

        for k in range(n):
            res += max(num1[k], num2[k])
        return int(res)


data = [1, 2, 2, 3, 3, 4]
f = Solution()
res = f.minnum(data)
print(res)








