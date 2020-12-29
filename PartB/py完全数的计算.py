
# 所谓完全数字，指的是数字的因子之和等于数字


while True:
    try:
        def checkPerfectNumber(num: int) -> bool:
            def getnum(A):
                list2 = []
                for i in range(1, A // 2 + 1):
                    if A % i == 0:
                        list2.append(i)
                return list2

            list3 = getnum(num)
            if num == sum(list3):
                return True
            else:
                return False

        n = int(input())
        num2 = 0
        for i in range(1, n+1):
            if checkPerfectNumber(i):
                num2 += 1
        print(num2)

    except:
        break


