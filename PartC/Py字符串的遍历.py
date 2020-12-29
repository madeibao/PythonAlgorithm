

1 直接进行遍历

strs = 'abcd'
for ch in strs:
    print(ch)


2 利用下标遍历


strs = 'abcd'
for index, ch in enumerate(strs):
    print(index,end=' ')
    print(ch)



3 利用range进行遍历

strs = 'abcd'
for index in range(len(strs)):
    print(strs[index], end=' ')


4 利用迭代器

strs = 'abcd'
for ch in iter(strs):
    print(ch)







