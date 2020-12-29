

a = list(map(int, input().split()))


def solve(l, r):  # 另一种思路和方法。
    if l == r:
        return a[l]
    ans = 0
    for i in range(l, r):
        lans = solve(l, i)
        rans = solve(i+1, r)   # 递归的写法。
        ans = max(ans, lans+rans)
        ans = max(ans, lans*rans)
    return ans


print(solve(0, 2))



今天上课，老师教了小易怎么计算加法和乘法，乘法的优先级大于加法，但是如果一个运算加了括号，那么它的优先级是最高的。例如： 1 2 3  
1+2*3=7 1*(2+3)=5 1*2*3=6 (1+2)*3=9 现在小易希望你帮他计算给定3个数a，b，c，在它们中间添加"+"， 
“*”， “(“， “)”符号，能够获得的最大值。




下面可以直接的暴力破解，这里提供了新的思路和见解。


a = list(map(int, input().split()))

def solve(i, j, k):
    ans1 = (i+j)+k
    ans2 = (i*j)+k
    ans3 = (i*j)*k
    ans4 = i+(j*k)
    ans5 = (i+j)*k
    ans6 = (i*j)+k
    print(max(ans1, ans2, ans3, ans4, ans5, ans6))


solve(a[0], a[1], a[2])
