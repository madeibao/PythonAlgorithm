# ['1', '2', '3']

# 反过来转换的过程为：
if __name__ == '__main__':
    a = [1, 2, 3]
    list(map(str, a))
    print(list(map(str, a)))

    a = ['1', '2', '3']
    list2 = list(map(int, a))
    print(list2)
    # [1,2,3]
