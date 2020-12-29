"""
import operator
sortedDistIndicies=[3,2,1,0]
#labels = ['A', 'B', 'C', 'D']
labels = ['A', 'A', 'B', 'B']

classCount = {}          # 创建的是一个空的字典。
for i in range(4):
    voteIlabel = labels[sortedDistIndicies[i]]
    classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  # 逆序的值
print(sortedClassCount[0][0])

"""

import operator

dict={}

dict['A']=1
dict['B']=3
dict['C']=5
dict['D']=7
dict['E']=9
dict['F']=11
Countlabels_max=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)    # 根据第几个域进行排序。 所以，降序排列。
print(Countlabels_max)

