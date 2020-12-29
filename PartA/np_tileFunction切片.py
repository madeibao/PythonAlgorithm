
from numpy import *
import operator
group = array([[1.0, 1.1],
			   [1.0, 1.0],
			   [0,     0],
			   [0,   0.1]])
labels = ['A', 'A', 'B', 'B']

inX =[0.1, 0.1]
dataSetSize = group.shape[0]  		           # 返回的是一共有几行的操作。
diffMat = tile(inX, (dataSetSize, 1)) - group  # tile 是瓦片的操作
print(diffMat)
print("-----------------")
sqDiffMat = diffMat ** 2 
print(sqDiffMat)
sqDistances = sqDiffMat.sum(axis=1)
print("******************")
print(sqDistances)
distances = sqDistances ** 0.5  
sortedDistIndicies = distances.argsort()
#    print(sortedDistIndicies) # 返回的是元素在原array中的下标

classCount = {}          # 创建的是一个空的字典。
for i in range(4):
    voteIlabel = labels[sortedDistIndicies[i]]
    classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # 逆序的值
print(sortedClassCount[0][0])

