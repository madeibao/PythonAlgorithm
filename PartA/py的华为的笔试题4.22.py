# python用隔板来分割字符串中的数组形式。

题目复述：
对于一列有m个正整数元素的数组，用k-1个隔板把该数组分成连续的k份，每一份均非空。
找出一种分法，使得这k份中每份求和的最小值达到最大。
且若多种情况同时达到最优，那么找出一种使得靠近左侧部分的和更大的情况。最后输出原数组加分隔符'/'的形式。
比如一个数组100 200 300 400 500 600 700 800 900，将其分为3份，
那么100 200 300 400 500 / 600 700 / 800 900 这种分法的最小和是600+700=1300，且不存在其他分法使其更大。
再比如1 1 1 1 1 1 1 1，k=3。有6种分法达到最优：
1 1 / 1 1 1 / 1 1 1
1 1 1 / 1 1 / 1 1 1
1 1 1 / 1 1 1 / 1 1
1 1 / 1 1 / 1 1 1 1
1 1 / 1 1 1 1 / 1 1
1 1 1 1 / 1 1 / 1 1


那么让左侧部分尽量大，就输出 1 1 1 1 / 1 1 / 1 1。（即第一部分尽量大，若第一部分相同，则第二部分尽量大，以此类推）
输入：第一行m,k，分别表示数组元素个数与分割的份数；第二行一组正整数，为待分割数组。
输出：一行分割后结果，在分割点用' / '标出，如上面例子输出 1 1 1 1 / 1 1 / 1 1。


# 输入和输出的结果值：

9 3
100 200 300 400 500 600 700 800 900
100 200 300 400 500 / 600 700 / 800 900


m, k = tuple(map(int, input().split()))
nums = list(map(int, input().split()))
dp=[[0 for j in range(m)] for i in range(k)]

s=0
for i in range(m):
    s+=nums[i]
    dp[0][i]=s


for i in range(1,k):
    for j in range(i,m-k+i+1):
        t=nums[j]
        h=j
        if t>=dp[i-1][h-1]:
            dp[i][j] = dp[i - 1][h - 1]
        else:
            while t<dp[i-1][h-1] and h>i:
                u=t
                h-=1
                t+=nums[h]
            if t>=dp[i-1][h-1]:
                if u>=dp[i-1][h-1]:
                    dp[i][j]=u
                else:
                    dp[i][j]=dp[i-1][h-1]
            else:
                dp[i][j]=t


val=dp[-1][-1]
s=0
sp=[]
count=0
for i in range(m-1,-1,-1):
    s+=nums[i]
    if s>=val:
        s=0
        sp.append(i)
        count+=1
        if count==k-1:
            break
nums=list(map(str,nums))
n=len(sp)


for i in range(n):
    nums.insert(sp[i],'/')
print(' '.join(nums))




C+++的代码：

