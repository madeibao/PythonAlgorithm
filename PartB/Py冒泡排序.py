

def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数（比如说n个数，则只要进行n-1次冒泡，就可以把这个n个数排序好，对吧）
        for j in range(len(nums) - i - 1):  
        """
        这里这个j呢就是控制每一次具体的冒泡过程，请你想一想，我们第一次冒泡需要冒几次，也就是说需要比较几次，
        假如有三个数，那只需要两次就可以了，当下一次时，最后一个
        已经是有序的了，所以说少冒泡一次，所以这里j每次都会减去i的值，即不用冒“无用之泡泡”
        """    
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def bubblesort(nums):
    for i in range(len(nums) - 1):
        ex_flag = False  # 改进后的冒泡，设置一个交换标志位
        for j in range(len(nums) - i - 1):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                ex_flag = True

        if not ex_flag:
            return nums  # 这里代表计算机偷懒成功 (〃'▽'〃)
    return nums          # 这里代表计算机没有偷懒成功 o(╥﹏╥)o


list2 = [2, 1, 2, 3, 3, 4, 5, 6, 67, ]
print(bubblesort(list2))











