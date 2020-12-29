

def binary_search(list1,item):
    low = 0
    high= len(list1)-1

    while low <= high:
        mid = (low+high)//2
        guess = list1[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid-1
        else:
            low = mid+1
    return None


list1 = [1, 3, 4, 6, 8, 10, 11, 13]
print(binary_search(list1, 8))




def binary_search(list1, items):
    low = 0
    high = len(list1)-1

    while low <= high:
        mid = (low+high)//2
        if items == list1[mid]:
            return mid
        elif items < list1[mid]:
            high = mid-1
            return binary_search(low, high)
        elif items > list1[mid]:
            low = mid+1
            return binary_search(low, high)
    return None


list1 = [1, 2, 4, 6, 8, 10, 12, 14, 18, 19, 20]   # 必须是有序的数组才能够进行二分查找。
print(binary_search(list1, 10))





def binary_search(arr,target):
    start,end = 0,len(arr)-1
    while True:
        if end - start <=1:
            if target == arr[start]:
                return(start)
            elif target == arr[end]:
                return(end)
            else:
                return(-1)

        mid = (start + end)//2
        if arr[mid]>=target:
            end = mid
        else:
            start = mid
            

#print(binary_search([1,4,7,8,9,12],9))
#print(binary_search([1,4,7,8,9,12],3))
in_put=list(map(int,input().split(',')))
in_index=int(input())
print(binary_search(in_put,in_index))


# 依照逗号进行数组的分割，第二个输入的是待查找的元素。































