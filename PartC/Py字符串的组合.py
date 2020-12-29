


abc 的组合

a
b
c

ab 
ac
bc

abc


s = input()
s = list(s)
for i in range(0,len(s)+1):
    words = []
    for j in range(0, len(s)):
        #for p in range(i,len(s)+1):
        if(j+i<len(s)+1):
            t = ''.join(s[j:j+i])
            if t not in words:
                words.append(t)
    words.sort()
    print(' '.join(words),end=' ')


