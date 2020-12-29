

def bubbleSort(list2):

    for i in range(len(list2)-1):
        for j in range(len(list2)-i-1):
            if list2[j] > list2[j+1]:
                list2[j], list2[j+1] = list2[j+1], list2[j]
    return list2


if __name__ == '__main__':
    list2 = [1, 3, 1, 2, 3, 8, 4, 5, 6]
    print(list2)
    for i in bubbleSort(list2):
        print(i, end=' ')


"""
刚开始想的是：第二个循环采用for j in range(i+1,len(list)-1),但是在写交换比较时，会用到当层固定的list[i]，不合理
这里采用到的是，在第i次循环下，比较j 和j+1的元素大小，进行比较交换，排序。
"""
