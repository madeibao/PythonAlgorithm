

# -*- coding: utf-8 -*-

第一题 模拟找钱
假设咖啡卖 5 元，每个客户可能给你 5、10、20 元的纸币，初始情况下你没有任何纸币，问是否能够找零。
如果能找零就输出 true，总用户数， 否则输出 false,失败的用户index。
例如：
5,5,5,10 => true,4
10,10 => false,1

from typing import List


def run1():
    moneys = list(map(int, input().split(',')))
    number_of_5 = 0
    number_of_10 = 0
    number_of_20 = 0
    for index, value in enumerate(moneys):
        if value == 5:  # ok
            number_of_5 += 1
            continue
        elif value == 10:  # return 5
            number_of_10 += 1
            number_of_5 -= 1
            if number_of_5 < 0:
                print('false,'+str(index + 1))
                return
        elif value == 20:  # return 15
            number_of_20 += 1
            if number_of_10 > 0 and number_of_5 > 0:
                number_of_10 -= 1
                number_of_5 -= 1
            elif number_of_5 > 0:
                # 必须是三张5元的硬币才能够找开。
                number_of_5 -= 3
                if number_of_5 < 0:
                    print('false,'+str(index + 1))
                    return
            else:
                print('false,'+str(index + 1))
                return
        # 硬币只能有 5，10，20的三种的选择。
        else:
            print('false,'+str(index + 1))
            return

    # 默认的条件下的返回的结果值。
    print('true,'+str(len(moneys)))


if __name__ == '__main__':
    run1()







#---------------------------------------------------------------------------------------------------------------------------------


def run1():
    moneys = list(map(int, input()[1:-1].split(',')))
    number_of_5 = 0
    number_of_10 = 0
    number_of_20 = 0
    for index, value in enumerate(moneys):
        if value == 5:  # ok
            number_of_5 += 1
            continue
        elif value == 10:  # return 5
            number_of_10 += 1
            number_of_5 -= 1
            if number_of_5 < 0:
                print('false')
                return
        elif value == 20:  # return 15
            number_of_20 += 1
            if number_of_10 > 0 and number_of_5 > 0:
                number_of_10 -= 1
                number_of_5 -= 1
            elif number_of_5 > 0:
                # 必须是三张5元的硬币才能够找开。
                number_of_5 -= 3
                if number_of_5 < 0:
                    print('false')
                    return
            else:
                print('false')
                return
        # 硬币只能有 5，10，20的三种的选择。
        else:
            print('false')
            return

    # 默认的条件下的返回的结果值。
    print('true')


if __name__ == '__main__':
    run1()
