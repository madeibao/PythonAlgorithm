def inertsort(l):  #参数的传入，当想传入的是一个list时，直接传入一个变量就行了
    N=len(l)
    for x in range(1,N):
        a,b=x,x
        n=l[x]
        while n<l[a-1] and a-1>=0:
            a=a-1
            if a-1<0:
                a=0 
        while b>a:
            l[b]=l[b-1]
            b=b-1
        l[a]=n

l=[1,3,2,8,5,3,1]
inertsort(l)
print(l)

