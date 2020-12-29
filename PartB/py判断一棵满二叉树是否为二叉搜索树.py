




tmp = input()
if tmp == 'None':
    print(True)
    exit()

arr = list(map(int, tmp.split(',')))
# 变成列表的形式来存储。
n = len(arr)
 
def check(arr, k, n, left, right):
    if k >= n:
        return True
    if arr[k] <= left or arr[k] >= right:
        return False
    if not check(arr, 2*k+1, n, left, arr[k]) or not check(arr, 2*k+2, n, arr[k], right):
            return False
    return True
 
if n < 2:
    print(True)


print(check(arr, 0, n, -float('inf'), float('inf')))

#------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

def isBST(nums):
    for i in range(len(nums)//2-1,-1,-1):
        l=2*i+1
        r=2*i+2

        if l<len(nums) and nums[l]>nums[i]:
            return False
        if r<len(nums) and nums[r]<nums[i]:
            return False

        if i%2 and r<len(nums):
            nums[i]=nums[r]

        if not i%2 and l<len(nums):
            nums[i]=nums[l]

    return True


strs=input().strip()
if strs=='None':
    print('True')
else:
    nums=list(map(int,strs.split(',')))
    print(isBST(nums))


# 10,5,15,3,7,13,18



