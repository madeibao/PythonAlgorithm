

n = int(input())
list2 = list(map(int, input().split(" ")))
res = 0

for i in list2:
    if i<0:
        continue
    elif i%2==0:
        res+= i//2;
    else:
        if i==1:
            continue
        else:
            res+=(i-3)/2+1
print(res)

