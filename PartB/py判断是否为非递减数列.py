

def reduce(strs):
    res = 0
    for i in range(1, len(strs)):
        if strs[i]-strs[i-1]>=0:
            continue
        else:
            res+=1

    if res<=1:
        return True
    return False


if __name__=='__main__':
    nums = list(map(int, input().split(" ")))
    if reduce(nums):
        print(1)
    else:
        print(0)









