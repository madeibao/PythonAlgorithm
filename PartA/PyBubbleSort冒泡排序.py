L = [8,2,50,3]

def bubble_sort(L):
    for i in range(len(L)-1):				#循环次数
        for j in range(len(L)-i-1):			#下标
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]    # 两个值的互换的操作。
    return L


print(bubble_sort(L))