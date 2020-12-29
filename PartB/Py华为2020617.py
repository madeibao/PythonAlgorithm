
def exchange(str3):
    list2 = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    map2 = dict(Counter(str3))
    list3 = list(str3)

    for i in list3:
        if i in list2 and map2.get(i)>1:
            list3.remove(i)
        else:
            continue
    return "".join(list3)


def normallize(name):
    return name.capitalize()


list3 = input().lower().split(" ")

res = []
for i in list3:
    res.append(exchange(i))

res2 = []
for i in res:
    res2.append(normallize(i))

print(" ".join(res2))

