

capicaty=[0,1,2]
value=[0,1,2]

def  best_value(i,j):
    if i==0:
        return 0
    if j-capicaty[i]<0:
        return best_value(i-1,j)
    else:
        return max(best_value(i-1,j),best_value(i-1,j-capicaty[i])+value[i])



print(best_value(2,2))

