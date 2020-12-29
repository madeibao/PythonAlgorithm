签到用户最多的三个目的地以及签到的用户数
同一个用户多次签到同一个城市，只记一次。
签到用户数字相同的城市，优先展示按照字母表排序所得到的城市名字。

以下是输入数据，数字编号代表的是用户ID编号

123-beijing 123-shanghai 124-hongkong 124-guilin 124-guilin 125-shanghai 125-shanghai 126-nanjing

输出结果为：
最终的输出结果为：
 shanghai 2
 beijing 1
 guilin 1

#---------------------------------------------------------------------------------	

num = input()
list1 = num.split(" ")     # 按照空格进行分割开来。
list2 = list(set(list1))   # 利用集合去除重复的签到，然后再转化成列表的形式进行过存储。


city = []   # 建立城市列表，统计不同的用户的城市的访问

for i in range(len(list2)):
    city.append(list2[i].split("-")[1])

# 用字典统计城市，以及城市的访问的次数。
counts = dict()
for i in city:
    counts[i] = counts.get(i, 0) + 1

# {'beijing': 1, 'hongkong': 1, 'nanjing': 1, 'shanghai': 2, 'guilin': 1}

# 下面利用字典的多条件进行排序。
# 先按照签到次数多的城市，然后按照字母顺序表进行排序。


sort2 = sorted(counts.items(), key=lambda s: (-s[1], s[0]))
for i in sort2[:3]:
    print(' '.join(map(str, list(i))))

# 打印输出结果值。







