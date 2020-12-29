

# # 给定一个数组和一个目标值，
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 第一行的暴力破解的方法，
# 第一种的解法：



def twoSum(nums, target):
    lens = len(nums)
    j = -1
    for i in range(1, lens):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
            
    if j >= 0:
        return [j, i]


def twoSum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum(nums, target):
    hashmap = {}  # 利用python的字典的写法。   
    for i, num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target - num)]
        hashmap[num] = i    # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况



print(twoSum([2, 7, 11, 15], 9))
