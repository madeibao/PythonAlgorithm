


import numpy as np
x=np.array([1,4,3,-1,6,9])
print(x.argsort())


2.现在我们可以看看argsort()函数的具体功能是什么：

输出定义为y=array([3,0,2,1,4,5])。

我们发现argsort()函数是将x中的元素从小到大排列，提取其对应的index(索引)，然后输出到y。例如：x[3]=-1最小，所以y[0]=3,x[5]=9最大，所以y[5]=5。