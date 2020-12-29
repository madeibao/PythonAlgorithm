d = {'a': 2, 'b': 3, 'd': 4}
dlist=list(d.keys())
print(dlist)
# ['a', 'd', 'b']






# 获得字典的的所有的键的方法
dates = {'Sun': '星期天', 'Mon': '星期一', 'Tues': '星期二', 'Wed': '星期三', 'Thurs': '星期四', 'Fri': '星期五', 'Sat': '星期六'}
day = dates.get('Fri', '未知')         # 默认的情况下输出的是未知，如果前一部分都不存在的话。
print(day)                             # 输出结果为星期五




