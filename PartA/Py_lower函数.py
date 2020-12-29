
# 列表中的首字母大写，其他部分小写。


def change(name):
    result = name[0:1].upper()+name[1:len(name)].lower()
    return result


name_list = ['kzd', 'ysy', 'kcw', 'scr', 'ky']
name_li = list(map(change, name_list))
print(name_li)


# ['Kzd', 'Ysy', 'Kcw', 'Scr', 'Ky']