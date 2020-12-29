def innerFun_0():
    print("i am first innerFun")
    return    

def innerFun_1():
    print("i am second innerFun")
    return    

def outFun():   
    innerFun_0()  
    innerFun_1()   
    return

outFun()#调用outFun函数

# 结果：
# i am first innerFun
# i am second innerFun