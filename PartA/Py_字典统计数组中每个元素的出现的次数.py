
#----------------------------------------------------------------
iems = ['apple','red','apple','red','red','pear']

counts = dict()
for i in items:
  counts[i] = counts.get(i, 0) + 1



#  {1: 2, 2: 2, 3: 2, 4: 2, 5: 1, 7: 1, 8: 1}

from collections import Counter
list = [1,2,3,4,5,4,3,7,2,8,1]
num_Count=Counter(list)
print(num_Count)


list = [1,2,3,4,5,4,3,7,2,8,1]

num_count = {}
for i in list:
    if i not in num_count:
        num_count[i]=1
    else:
        num_count[i]+=1

print(num_count)


#----------------------------------------------------------------
# 另一种方法;
from collections import Counter
num = [1, 2, 3, 3, 2, 2, 4, 5, 1, 1, 1, ]
dict1 = Counter(num)
dict2 = dict(dict1)










