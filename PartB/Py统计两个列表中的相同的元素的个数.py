Anum = 0
list2 = [1, 1, 1, 1, 2, 2]
list3 = [2, 1, 1, 1, 1, 2]

list4 = list()
list5 = list()
counts2 = dict()
for i in list2:
  counts2[i] = counts2.get(i, 0) + 1

counts3 = dict()
for i in list3:
  counts3[i] = counts3.get(i, 0) + 1

for i in counts2:
    list4.append((i, counts2[i]))

for j in counts3:
    list5.append((j, counts3[j]))


for i, j in zip(list4, list5):
    if i[0] == j[0] and i[1] == j[1]:
        Anum += i[1]

print(Anum)


两个列表中的共同出现1四次，2两次，所有共同的元素的个数为6

结果返回6。

