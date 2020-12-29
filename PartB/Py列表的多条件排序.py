

a = [(1,2), (2,4), (1,3)]
a.sort(key=lambda elem: (elem[0], -elem[1]))
print(a)  # [(1, 3), (1, 2), (2, 4)]
 
 
# 或者
def my_key(x):
    return x[0], -x[1]
 
a = [(1,2), (2,4), (1,3), (5,3)]
a.sort(key=my_key)
print(a)  # [(1, 3), (1, 2), (2, 4)]


