定义一个列表，并将列表中的头尾两个元素对调。
例如： 
对调前 : [1, 2, 3]
对调后 : [3, 2, 1]

#----------------------------------------------------------------
def swapList(newList): 
    size = len(newList) 
      
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp 
      
    return newList 

newList = [1, 2, 3] 
  
print(swapList(newList))


# 方法二
def swapList(newList): 
      
    newList[0], newList[-1] = newList[-1], newList[0] 
  
    return newList 
      
newList = [1, 2, 3] 
print(swapList(newList))


# 方法三

def swapList(list): 
      
    get = list[-1], list[0]    # get是一个元组。
      
    list[0], list[-1] = get 
      
    return list
      
newList = [1, 2, 3] 
print(swapList(newList))




