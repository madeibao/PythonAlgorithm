#统计词频
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
result = {}
for color in colors:
    if result.get(color)==None:   # 如果是第一次见到这种情况。
        result[color]=1
    else:
        result[color]+=1
print (result)



#  {'red': 2, 'blue': 3, 'green': 1}


from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print(dict(c))

# 效果是一样的。  {'red': 2, 'green': 1, 'blue': 3}




from collections import Counter
cnt = Counter()    # 创建一个空的
c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))

# ['b', 'b', 'a', 'a', 'a', 'a']




