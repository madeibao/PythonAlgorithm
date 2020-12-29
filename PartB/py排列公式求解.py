



A(n,m) = n!//(n-m)!


def permutation(n, k):
    if k>n:
        return 0
    if k==0:
        return 1
    if k==1:
        return n
    res = 1
    while k>0:
        res*= n
        n-=1
        k-=1
    return res


print(permutation(5, 1))
