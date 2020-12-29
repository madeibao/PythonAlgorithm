 


 
def stringPowerSet(strs):
    N = len(strs)
    res = []
    for i in range(2 ** N):
        temp = ""
        for j in range(N):
            if (i>>j)%2:
                temp+=strs[j]
        res.append(temp)
    return res
 
 
if __name__ == '__main__':
    print(stringPowerSet("abc"))

