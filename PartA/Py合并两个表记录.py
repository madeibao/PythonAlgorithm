
4
0 1
0 2
1 2
3 4

#================================================================

0 3
1 2
3 4

#================================================================

from collections import defaultdict
while True:
    try:
 		# dd 为默认的字典内容。
        a,dd=int(input()),defaultdict(int)
        for i in range(a):
            key,val=map(int,input().split())
            dd[key]+=val
        for i in sorted(dd.keys()):
            print(str(i)+" "+str(dd[i]))
 
 
    except:
        break