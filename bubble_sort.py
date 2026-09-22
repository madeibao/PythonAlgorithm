def bubble_sort(arr):
    """冒泡排序:重复遍历列表,比较相邻元素,若顺序错误则交换。

    时间复杂度: O(n^2),最好情况(已排序) O(n)
    空间复杂度: O(1),原地排序
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # 优化:本轮若无交换,说明已有序
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("排序前:", data)
    bubble_sort(data)
    print("排序后:", data)
