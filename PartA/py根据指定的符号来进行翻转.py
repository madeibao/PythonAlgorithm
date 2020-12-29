

while True:
    try:
        num = int(input())
        list2 = list(map(int, input().split(" ")))
        flag = int(input())

        if flag==0:
            list2 = sorted(list2)
        else:
            list2 = sorted(list2, reverse=True)
        list3 = map(str, list2)
        print(" ".join(list3))

    except:
        break
        