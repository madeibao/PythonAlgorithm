

def get_num_factors(num):
    list0 = []
    tmp = 2
    if num == tmp:
        print(num)
    else:
        while num >= tmp:
            k = num % tmp
            if k == 0:
                list0.append(tmp)
                num = num / tmp  # 更新
            else:
                tmp = tmp + 1  # 同时更新除数值，不必每次都从头开始
    return list0


num = int(input())
list2 = get_num_factors(num)
print(list2)













