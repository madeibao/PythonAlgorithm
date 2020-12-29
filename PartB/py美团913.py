


def fun2(arr, k):
    cnt = 0
    for i in arr:
        if i >= k:
            cnt+=1
    if cnt==len(arr):
        return True
    return False


n, m, k = map(int, input().split(" "))
list2 = list(map(int, input().split(" ")))
cnt = 0
for i in range(len(list2)-m+1):
    temp = list2[i:i+m]
    if fun2(temp, k):
        cnt += 1

print(cnt)




