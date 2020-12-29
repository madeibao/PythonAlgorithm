

# 最初使用字典的时候，只是简单实用dict()，但是如果键不存在，就会报错显示keyerror，此时可以考虑使用defaultdict()函数。


import collections
bag = ['apple', 'orange', 'cherry', 'apple', 'apple', 'cherry', 'blueberry']
count = collections.defaultdict(int)
for fruit in bag:
    count[fruit] += 1

print(count)



#  defaultdict(<class 'int'>, {'apple': 3, 'cherry': 2, 'orange': 1, 'blueberry': 1})

















