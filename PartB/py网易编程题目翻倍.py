


n=int(input())
for i in range(n):
    a,b,p,q=map(int,input().split())
    k=0
    while(a<b):
        if(a+p>=b):
            a=a+p
        else:
            p=p*q
        k=k+1
    print(k)



