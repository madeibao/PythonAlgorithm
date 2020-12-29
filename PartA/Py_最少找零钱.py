money = [25, 10, 5, 1]  # 硬币种类


def coin(e):
    print("顾客给了:" + str(e) + "分")
    n = [0, 0, 0, 0]  # 存储硬币种类次数
    while e > 0:
        if e >= money[0]:
            e = e - money[0]
            n[0] = n[0] + 1
        elif money[1] <= e < money[0]:
            e = e - money[1]
            n[1] = n[1] + 1
        elif money[2] <= e < money[1]:
            e = e - money[2]
            n[2] = n[2] + 1
        elif money[3] <= e < money[2]:
            e = e - money[3]
            n[3] = n[3] + 1
    print("两角五分" + str(n[0]) + "个")
    print("一角" + str(n[1]) + "个")
    print("五分" + str(n[2]) + "个")
    print("一分" + str(n[3]) + "个")
    s = n[0] + n[1] + n[2] + n[3]
    print("所以最少找零个数是:" + str(s))


coin(63)