


# 用一个字典来统计列表中的出现的元素的次数。


iems = ['apple', 'red', 'apple', 'red', 'red', 'pear']

counts = dict()
for i in items:
  counts[i] = counts.get(i, 0) + 1


#  {'pear': 1, 'apple': 2, 'red': 3}


#------------------------------------------------------------------------

第二种方法内容

list1=[1,3,2,4,2,3]

dict_cnt={}   #dict_cnt=dict()

for item in list1:

   if item in dict_cnt: #直接判断key在不在字典中

      dict_cnt[item]+=1

   else:

      dict_cnt[item]=1

      
# 第三种方法内容：

方法二：利用collections中的defaultdict()

defaultdict()可以接受一个参数，如str，int，float等。
但这个参数并不是来约束字典的key的值的类型，也不是用来约束value的值的类型。
而是当字典的key不存在时，将value初始化为某个值。str初始化为“”，int初始化为0，float初始化为0.0。


from collections import defaultdict

list1=[1,2,3,4,3,2]

count_dict=defaultdict(int)

for item in lists:

   count_dict[item]+=1







