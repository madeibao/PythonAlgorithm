

def findSameNum(num1, num2):   # 判断两个数组中是否出现相同的元素内容。首先两个数组已经排好序列。
    i = j = 0
    while i <= len(num1) - 1 and j <= len(num2) - 1:
        if num1[i] == num2[j]:
            return True
        if num1[i] <= num2[j]:
            i += 1
        else:
            j += 1
    return False


if __name__ == "__main__":
    num1 = [1, 2, 3, 4, 5]
    num2 = [5, 6, 7, 8]
    print(findSameNum(num1, num2))


# 注意的是两个数组中的元素已经排好序列。



