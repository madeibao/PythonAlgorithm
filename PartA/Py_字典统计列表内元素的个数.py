


items = ['apple','red','apple','red','red','pear']
counts = dict()
for i in items:
  counts[i] = counts.get(i, 0) + 1


#  {'pear': 1, 'apple': 2, 'red': 3}



# 方案2的解法。
from collections import Counter
iems = ['apple','red','apple','red','red','pear']

# 
dict2 = dict(Counter(iems))
print(dict2)


