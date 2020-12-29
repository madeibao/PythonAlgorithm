
题目：一个数组代表股票每天的价格，可以选择从某一天买入，然后之后的一天卖出，求能够获得的最大收益。

[3,4,5,6,5,8]，
输出为5（在价格为3的时候买入，在价格为8的时候卖出）
输入为
[3,4,5,6,7,2,8]
输出为6（在价格为2时买入，在价格为8时卖出）



def our_solution(array):
    max_out=0
    temp=0
    for i in range(1,len(array)):
        temp+=array[i]-array[i-1]
        if temp>max_out:
            max_out=temp
        elif temp<0:
            temp=0
    return max_out


print(our_solution([3,4,5,6,5,8]))












