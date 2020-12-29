
>>> a = [1,2,3]

>>> b=[1,2]

>>> ####################################

>>> #两个列表的差集

>>> ret = []

>>> for i in a:

	if i not in b:

	     ret.append(i)

>>> ret

[3]

>>> #两个列表的差集2

>>> ret2 = [ i for i in a if i not in b ]

>>> ret2

[3]

>>> #两个列表的差集3

>>> ret3 = list(set(a) ^ set(b))

>>> ret3

[3]

>>> #两个列表的差集4

>>> ret4=list(set(a).difference(set(b))) #  b中有而a中没有的

>>> ret4

[3]



#----------------------------------------------------------------


>>> ########################################

>>> #获取两个list 的并集

>>> ret1=list(set(a).union(set(b)))

>>> ret1

[1, 2, 3]

>>> ret1=list(set(a).union(set([4,5,6])))

>>> ret1

[1, 2, 3, 4, 5, 6]

>>> #获取两个list 的并集2

>>> ret2= list(set(a) | set(b))

>>> ret2

[1, 2, 3]

>>> ret2=list(set(a)-set(b))#####差集

>>> ret2

[3]



#----------------------------------------------------------------
>>> ##########################################
>>> #获取两个列表的交集
>>> a = [1, 2, 3, 4, 5, 6]
>>> b = [2, 4, 6, 8 ,10]
>>> ret1= [x for x in b if x in set(a)]   # list a is the larger list b
>>> ret1
[2, 4, 6]
>>> #获取两个列表的交集2
>>> ret2= list(set(a) & set(b))
>>> ret2
[2, 4, 6]

>>> #获取两个列表的交集3
>>> ret3= list(set(a).intersection(b))
>>> ret3
[2, 4, 6]
>>>  #获取两个列表的交集4
>>> ret4 = list((set(a).union(set(b)))^(set(a)^set(b)))
>>> ret4
[2, 4, 6]

>>> 


