

def outFun():   
    def innerFun_0():	#1.在内部定义一个函数
        print("i am first innerFun")
        return    
    
    def innerFun_1():	#2.在内部定义另外一个函数
        print("i am second innerFun")
        return      
    
    innerFun_0()   #3.使用innerFun_0
    innerFun_1()   #4.使用innerFun_2
    
    return

outFun() 	#5.调用outFun函数


# 结果：
# i am first innerFun
# i am second innerFun






















