

 
 
import sys
n,t = map(int,sys.stdin.readline().strip("\n").split(" ") )
s=sys.stdin.readline().strip("\n")
 
for i in range(t):
    ops_type,ops_idx=map(int,sys.stdin.readline().strip("\n").split(" "))
    if ops_type==1:
        s=s[len(s)-ops_idx:len(s)]+s[0:len(s)-ops_idx]
    else:
        print(s[ops_idx])
 


 