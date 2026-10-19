from typing import List

def search(nums: List[int], target: int) -> bool:
    l = 0
    r = len(nums) - 1

    # 修复1：将 l < r 改为 l <= r，确保最后一个元素也能被检查到
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            print(f"找到了，下标为{mid}")
            return True
            # 修复2：删除了这里多余的 break
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    
    # 循环结束仍未找到，返回 False
    return False

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    target = 10
    print(search(nums, target))  # 输出: 找到了，下标为9 \n True