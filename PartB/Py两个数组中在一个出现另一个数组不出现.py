



[1,2,3,5]
[2,3,4,]

求得结果为[1,5]


def cha(list2, list3):
    res= []
    for i in list2:
        if i not in list3:
            res.append(i)

    return res


if __name__=="__main__":
    list2 =[1, 2, 3, 5]
    list3 = [2, 3, 4]
    print(cha(list2, list3))
