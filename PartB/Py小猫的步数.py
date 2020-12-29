


def minstep(n):
    if n<0:
        n=-n
    if n==0:
        return 0
    if n==1:
        return 1
    if n%2==0:
        return minstep(n//2)+1
    else:
        r1=minstep((n+1)//2)+2
        r2=minstep((n-1)//2)+2
        return min(r1,r2)

        
if __name__ =="__main__":
    n=int(input())
    print(minstep(n))
