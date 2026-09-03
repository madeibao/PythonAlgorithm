



def bubble_sort(nums):
    print('比较前的数据:',nums)
    num = len(nums)
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            print('第%d趟第%d次比较'%(i, j))
            print(nums)
    print('比较后的数据:',nums)


def bubble_sort_ex(nums):
    for i in range(len(nums) - 1):
        ex_flag = False  # 设置一个交换标志位
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                ex_flag = True
        if not ex_flag:
            return nums  # 已经有序了可以返回数据了

    return nums


if __name__ == '__main__':
    listData = [1, 10, 5, 9]
    bubble_sort_ex(listData)
    print(listData)