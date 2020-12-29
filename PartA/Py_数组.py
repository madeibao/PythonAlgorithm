





对于动态数组诸如创建、插入、删除、查询大小等操作，在C/C++语言中，可以使用标准库中的vector类实现，
而在python语言中，也同样提供了内置的array模块实现类似的功能。

Python中的array类似于列表list，如都可以动态增删元素，但又有所区别，list中存储的元素类型可以不一样，但array中元素类型必须完全一样。
另外，由于list中每个元素同时存储了其地址即指针（用以标记每个元素的数据类型）和实际的数据，所以，在存储及操作效率上，array又远远高于列表。


import array

arr = array.array('i', [0, 1, 1, 3])
print((arr.tolist()))

# [0, 1, 1, 3]

# array的效率要远高于array。
















