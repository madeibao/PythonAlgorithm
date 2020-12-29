
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        def getnum(A):
            list2 = []
            for i in range(1, A//2 + 1):
                if A % i == 0:
                    list2.append(i)
            return list2

        list3 = getnum(num)
        if num == sum(list3):
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkPerfectNumber(496))



# 如果一个数的所有的因子的和等于本身，就称次数为完美数字。

# 例如6  


# 封装的具体的函数内容。
def checkPerfectNumber(num: int) -> bool:

    def getnum(A):
        list2 = []
        for i in range(1, A//2 + 1):
            if A % i == 0:
                list2.append(i)
        return list2

    list3 = getnum(num)
    if num == sum(list3):
        return True
    else:
        return False


