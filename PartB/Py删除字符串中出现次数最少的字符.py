

# 删除字符串中出现次数最少的字符，如果多个字符的出现次数一致，都删除。
# 例如：	       abcdd	  
# 输出结果为    dd 

from collections import Counter

while True:
    try:
        s = input()
        # 利用字典来统计出现的次数。
        dict1 = Counter(s)
        dict2 = dict(dict1)

        # 按照值进行排序,字典的排序。
        sort = sorted(dict2.items(), key=lambda e: e[1])
        num = (sort[0][1])
        str1 = ""
        for key, value in sort:
            if value == num:
                str1 += key

        str2 = ""
        for i in s:
            if i in s and i not in str1:
                str2 += i
        print(str2)
    except:
        break


#通过默认的字典来排序进行。
#----------------------------------------------------------------


from collections import defaultdict
while True:
    try:
        a = input()
        dd = defaultdict(int)
        for i in a:
            dd[i] += 1
        for i in dd:
            if dd[i] == min(dd.values()):
                a = a.replace(i, "")
        print(a)
    except:
        break







