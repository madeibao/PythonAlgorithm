

lst = input().split()
lst1 = []
lst2 = []
for per_str in lst:
    if int(per_str) & 1 == 1:
        lst1.append(per_str)
    else:
        lst2.append(per_str)
print(" ".join(lst2), end = " ")
print(" ".join(lst1))




