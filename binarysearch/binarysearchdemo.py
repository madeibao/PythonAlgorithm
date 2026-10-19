



from collections import deque
from typing import List

def search(nums: List[int], target: int) -> bool:

    l = 0
    r = len(nums) - 1

    while l<r:
        mid = l+(r-l)//2
        if nums[mid] == 10:
            print(f"找到了，下标为{mid}")
            return True
            break
        elif nums[mid] < 10:
            l = mid + 1
        else:
            r = mid - 1
    return False

if __name__ == "__main__":

    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    target = 10


    print(search(nums, target))




















































