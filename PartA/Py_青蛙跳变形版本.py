

# 青蛙一次只能够跳1个或者是3个楼梯
# 求给定一定高度的楼梯的需要跳的次数。
# 下面给定了3个版本的内容。


 
# n = int(input())
# x,y,z=1,1,2
# for i in range(1,n-2):
#     x,y,z=y,z,x+z
# print(z)


# n = int(input())
# dp = [0]*(n+1)
# dp[1]=1
# dp[2]=1
# dp[3]=2
# for i in range(4,n+1):
#     dp[i]=dp[i-1]+dp[i-3]
# print(dp[n])


n=int(input().strip())
dp=[1,1,1]
for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-3])
print(dp[n])




