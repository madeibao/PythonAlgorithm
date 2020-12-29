

# 表达式的求值，没有运算符的优先级，只有先后出现的顺序。



import sys
s=sys.stdin.readline().strip()
n=len(s)
res=int(s[0])
for i in range(1,n):
    if s[i]=='+':
        res+=int(s[i+1])
    if s[i]=='-':
        res-=int(s[i+1])
    if s[i]=='*':
        res*=int(s[i+1])
    # 每次增加两个数字
    i+=2
print(res)




