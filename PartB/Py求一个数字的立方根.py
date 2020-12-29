


def find(n):
    res=n/2
    lower=0
    upper=n
    while abs(res**3-n)>0.0001:
        if res**3==n:
            return res
        elif res**3<n:
            lower=res
        else:
            upper=res
        res=(upper+lower)/2
    return res
 
n=float(input())
res=find(n)
print("%.1f" %res)













