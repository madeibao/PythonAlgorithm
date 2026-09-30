


list = [1,2,3,4,5,4,3,7,2,8,1]

num_count = {}
for i in list:
    if i not in num_count:
        num_count[i]=1
    else:
        num_count[i]+=1

print(num_count)

print("----------------------------")
list2 = [1,1,1,2,2,2,3,3,4,5,6]
dict2 = {}
for i in list2:
    dict2[i] = dict2.get(i,0)+1
print(dict2)


