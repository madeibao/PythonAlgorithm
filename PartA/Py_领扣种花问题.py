假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True


示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False


注意:


    数组内已种好的花不会违反种植规则。
    输入的数组长度范围为 [1, 20000]。
    n 是非负整数，且不会超过输入数组的大小。
#----------------------------------------------------------------
#@---------------------------------------------------------------

def canPlaceFlowers(flowerbed, n):
    N = len(flowerbed)
    for i in range(N):
        if n == 0:
            break
        if flowerbed[i] == 0:
            # 如果是第一个元素, 则需要判断两种情况:
            # 1. 只有一朵花
            # 2. 后一朵花为0
            if i == 0:
                if N == 1 or flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            # 如果是最后一个元素, 则判断前一个元素是否为0
            elif i == N - 1:
                if flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            # 否则是中间元素, 则判断前后是否等于0
            elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

    return n == 0

print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))





