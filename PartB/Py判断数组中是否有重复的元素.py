def judgeRepeated(array):
    nums = {}
    for i in array:
        if i not in nums:
            nums[i] = True
        else:
            return True
    return False


arr = [12, 22, 34, 45, 3, 44, 23, 23, ]   # 判断数组中是否有重复的元素。
print(judgeRepeated(arr))





# 利用python的集合来进行判断。
# def judgeRepeatedThird(array):
#     if len(set(array))==len(array):
#         return False
#     else:
#         return True
# 另外的一种实现形式。

