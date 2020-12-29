


def Selectionsort1(A):
    for i in range(len(A)):
        min = i
        for j in range(i + 1, len(A)):  # 上一个值右边的数组
            if A[min] > A[j]: 		    # 使min为最小值，遇到比min小的值就赋值于min
                min = j
        A[i], A[min] = A[min], A[i]     # 交换最小值到左边
    return A


list2 = [2, 1, 2, 3, 3, 4, 5, 6, 67]
print(Selectionsort1(list2))












