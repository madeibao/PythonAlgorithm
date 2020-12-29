假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。
可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。
能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1输出: True

示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2输出: False

注意:

数组内已种好的花不会违反种植规则。
    输入的数组长度范围为 [1, 20000]。
    n 是非负整数，且不会超过输入数组的大小。

#==================================================================

class Solution():
    def plant(self,nums,n):

        # 代表的是数组的长度。
        N = len(nums)
        for i in range(N):
            # 如果能够种完所有的花，返回真。
            if n==0:
                break
            # 首先此处没有花朵。
            if nums[i]==0:
                if i==0:
                    # 花坛的长度为1 或者是长度为2，且都没有种花。
                    if N==1 or nums[i+1]==0:
                        nums[i]=1
                        n-=1
                #如果下标来到了最后的一个位置内容。并且前面的位置也没有花朵。
                elif i==N-1:
                    if nums[i-1]==0:
                        nums[i]=1
                        n-=1

                # 前后的都没有花朵。
                elif nums[i-1]==0 and nums[i+1]==0:
                    nums[i]=1
                    n-=1
        return n==0


#-----------------------------------------------------------------

if __name__=='__main__':
    nums= [0, 0, 1]
    n=1

    s = Solution()
    print(s.plant(nums,n))