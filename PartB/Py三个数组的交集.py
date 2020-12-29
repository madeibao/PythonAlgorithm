
# 三个数组的交集内容。
# 也就是三个数组中都共同的出现的部分内容。

class Solution():
    def getinsect(self, list1, list2, list3):
        arr = list1+list2+list3
        res = []
        for i in arr:
            if arr.count(i)==3 and i not in res:
                res.append(i)

        return res


if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 5, 6, 7]
    c = [1, 3, 4, 5, 8]

    print(s.getinsect(a, b, c))
















