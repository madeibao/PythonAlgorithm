


enumerate函数用于遍历序列中的元素以及它们的下标,多用于在for循环中得到计数,enumerate参数为可遍历的变量，如字符串，列表等
一般情况下对一个列表或数组既要遍历索引又要遍历元素时，会这样写：
for i in range (0,len(list)): 
  print(i ,list[i])
但是这种方法有些累赘，使用内置enumerrate函数会有更加直接，优美的做法，先看看enumerate的定义：



enumerate会将数组或列表组成一个索引序列。使我们再获取索引和索引内容的时候更加方便如下：
for index，text in enumerate(list): 
  print(index, text)



mylist = ["a", "b", "c", "d"]
list2 = [(i, j) for i, j in enumerate(mylist)]
print(list2)



总结来说，就是一个列表，数组，既要遍历索引，又要遍历元素的时候，可以用enumerate的方法。


#------------------------------------------------------------------------------------------------



values=['a','b','c']

for index, element in enumerate(values):

    print ("the result of index is %d,the result of element is %s" % (index,element))

#============================================================================


the result of index is 0,the result of element is a
the result of index is 1,the result of element is b
the result of index is 2,the result of element is c

























