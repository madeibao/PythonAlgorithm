


# 利用Python的字典来统计符串中的每个字母的出现的次数。


from collections import Counter
s = 'sqwjodiqdjpneqonfpi23jpjp32pej3p'
dict1 = Counter(s)
dict2 = dict(dict1)
print(dict2)


#  {'2': 2, 'n': 2, 'e': 2, 'p': 6, 'f': 1, 'w': 1, 'o': 2, 'd': 2, '3': 3, 'i': 2, 's': 1, 'q': 3, 'j': 5}





























