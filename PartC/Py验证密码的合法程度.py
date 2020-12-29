
import sys

lst = list()
while True:
    str = sys.stdin.readline().strip()
    if str == "":
        break
 
    if len(str) <= 8:
        lst.append('NG')
        continue
 
    error = False
    for i in range(len(str) - 5):
        if str.find(str[i:i+3], i+3) >= 0:
            error = True
            break
    if error:
        lst.append('NG')
        continue;
 
    d ={'A': 0, 'a': 0, '8':0, '!':0}
    for chr in str:
        if 'A' <= chr <= 'Z':
            d['A'] = 1
        elif 'a' <= chr <= 'z':
            d['a'] = 1
        elif '0' <= chr <= '9':
            d['8'] = 1
        else:
            d['!'] = 1
    if sum(list(d.values())) >= 3:
        lst.append('OK')
    else:
        lst.append('NG')
 
for str in lst:
    print(str)


