
# 最长连续递增序列
# 这种情况只是针对的全都为正数的情况。


def method1(arr):
    temp, maxl, end = 1, 0, 0


    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            temp += 1
        else:
            temp = 1

        if temp > maxl:
            maxl = temp
            end = i


    print(maxl)  # 返回最大的连续递增子序列的长度值。
    list2 = arr[end+1-maxl:end+1]   # 返回的是这个列表的区间。
    return list2


print(method1([1, 9, 2, 5, 7, 3, 4, 6, 8, 0, 11, 15, 17, 17, 10]))

#-------------------------------------------------------------------------------
#===============================================================================


# 非连续的递增的子序列，得到最终的长度值
# 下面的条件不一定是连续的子序列。

import bisect
def lengthOfLIS(nums):
    q=[]
    for v in nums:
        print(q)
        pos=bisect.bisect_left(q,v)
        if pos==len(q):
            q.append(v)
        else:
            q[pos]=v

    return len(q)
  
print(lengthOfLIS(map(int,input().split())))

# 输入:    1 -1 2 -2 3 -3 4













