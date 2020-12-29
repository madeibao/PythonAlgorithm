
def sumID(num1,comID):
    list1 = []
    for i in range(num1):
    # for i in range(len(comID)):
        list1.append(''.join(sorted(list(comID[i]))))
# 字符串数组的组内字符进行排序，每个数组内的字符串都进行按照字母顺序进行排序。
    dict = {}   # 建立一个空的字典。
    for it in list1:
        if it not in dict:
            dict[it] = 1
        else:
            dict[it] += 1
'''
    counts = dict()
    for i in list1:
        counts[i] = counts.get(i, 0) + 1
'''
# 用字典存储相同的字符串出现的次数。
    list3 = []
    for key in dict:
        if dict[key] > 1:     # 如果出现次数多于一次
            list3.append(key)
# 建立一个列表存储的是字符串数组中出现次数大于1的那些字符串。
    b = []
    for j in range(len(list3)):
        a = []   # 每次都建立一个空列表。
        for i in range(len(comID)):
            if comID[i]==list3[j] or set(comID[i]) == set(list3[j]):
                a.append(comID[i])
        b.append(a)
    print(b)
    return b

num1 = 7
comID = ["abcd", "zesa", "saze", "abc", "pqrst", "cdab", "bacd"]
sumID(num1, comID)




'''
题目的大致意思是：
超市卖东西，然后统计那些商品相同的组合。
例如“abcd” 与“bacd” 是不同商品的组合，可以归于同一个类别；
要求统计出，出现次数多于一次的商品组合类别，有助于帮助商家进行决策，来更好的促销。


num1 = 7
comID = ["abcd", "zesa", "saze", "abc", "pqrst", "cdab", "bacd"]

给定参数1    num1 代表的是所有的商品列表总数量

参数2是一个列表，表示的是所有的商品的明细列表。

最终得出的结果为[["abcd","cdab", "bacd"],[ "zesa", "saze"]]

只有这两个不同的商品组合类别出现次数多于一次，依照列表的列表来进行统计。

注意，前方高能，我要发大招了，开个玩笑。

#---------------------------------------------------------------------------------------------------------------------------------------------

'''


