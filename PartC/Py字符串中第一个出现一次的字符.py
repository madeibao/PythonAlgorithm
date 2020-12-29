


# 找出字符串中第一个只出现一次的字符



while True:
    try:
        res = input()
        count = []
        for i in res:
            if res.count(i) ==1:
                count.append(i)
        if count:
            print(count[0])
        else:
            print(-1)
    except:
        break




# # asdfasdfom
# # aabbccddeeff

# from collections import Counter
# s = input()
# dict1 = Counter(s)
# dict2 = dict(dict1)

# list2 = []

# for key in dict2.keys():
#     if dict2[key] == 1:
#         list2.append(key)

# if list2:
#     for i in list(s):
#         if i in list2:
#             print(i)
#             break
# else:
#     print(-1)




