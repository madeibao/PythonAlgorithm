
# 给定列表之内的一串数字，然后统计列表内的这串数字中只是出现一次的数字的内容。


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counts = dict()
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        sort = sorted(counts.items(), key=lambda e: e[1])
        list2 = []
        for k, v in sort:
            if v == 1:
                list2.append(k)

        return list2[0]


    #方法2 是异或运算。
    def singleNumber2(self, nums: List[int]) -> List[int]:
        a = 0
        for num in nums:
            a = a ^ num
        return a


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 2, 1, 3, 2, 5]))







