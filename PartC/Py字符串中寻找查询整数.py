

import re

s1=[]
s3=[]
a='{2020/06/23}3(ORA-7401)'
s=re.findall('[-|0-9]+',a)
print(s)
for x in s:
    n=int(x)
    s1.append(int(x))
s2=sorted(s1,reverse=True)

s3 = list(map(str, s2))
print(",".join(s3))


'''
for y in s2:
    m=str(y)
    s3.append(m)
output=','.join(s3)
print(output)
'''