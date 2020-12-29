



a,b=map(int,input().split())
s=str(a//b)
a=a%b
if a>0:
    s+='.'
pos=len(s)
d={a:pos}

flag=0


while a!=0:
    s+=str(a*10//b)
    a=a*10%b
    if a not in d:
        pos+=1
        d[a]=pos
    else:
        s=s[:d[a]]+'('+s[d[a]:]+')'
        break


print(s)


