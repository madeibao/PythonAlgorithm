res = []
def find(a,b,c):
    if not a and not b:
        res.append(' '.join(map(str,c)))
    if b:
        c.append(b.pop())
        find(a,b,c)
        b.append(c.pop())
    if a:
        b.append(a.pop(0))
        find(a,b,c)
        a.insert(0,b.pop())

        
  
n = input()
n = int(n)
pre = list(map(int,input().split()))
ins,outs = [],[]
find(pre,ins,outs)
res.sort()
for i in res:
    print(i)





