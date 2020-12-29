
# 重复字符排序
# 题目描述：找出输入字符串中的重复字符，再根据ASCII码把重复的字符从小到大排序。

# 例如：输入ABCABCdd，输出ABCd。



# 找出字符串中的重复的字符，来进行排序

from collections import Counter
str2 = input()
dict2 = dict(Counter(str2))
res = []

for i in list(str2):
    if dict2.get(i)>1:
        res.append(i)
    else:
        continue
res.sort()
print("".join(res))



