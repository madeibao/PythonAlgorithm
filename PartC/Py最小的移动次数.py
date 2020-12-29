

n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
res=0
for i in range(0,len(a)):
    if(a[i]!=b[i]):
        res+=1
print(res)


