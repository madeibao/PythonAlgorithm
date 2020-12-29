
# 题目描述
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。


class Solution():
    def count(self, items):
        counts = dict()
        length = len(items)
        for i in items:
            counts[i] = counts.get(i, 0) + 1

        for key in counts:
            if counts[key] > length/2:
                return key
            else:
                return 0


if __name__ == "__main__":
    # list2 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    nums = list(map(int,input()[1:-1].split(',')))
    s = Solution()
    print(s.count(nums))


# 方法2的结果，非常的巧妙

nums = list(map(int,input()[1:-1].split(',')))
for i in nums:
    if nums.count(i) > len(nums)//2:
        break
print(i)


