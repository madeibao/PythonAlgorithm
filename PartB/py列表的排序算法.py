


from functools import cmp_to_key

nums = [3, 30, 34, 5, 9]


# 降序排序。
new_nums = sorted(nums, key=cmp_to_key(lambda x, y: y - x))
new_nums2 = sorted(nums, key=cmp_to_key(lambda x, y: x - y))
print(new_nums)
print(new_nums2)
#结果:
#[34, 30, 9, 5, 3]
#[3, 5, 9, 30, 34]



