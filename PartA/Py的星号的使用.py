

def foo(param1, *param2):
    print (param1)
    print (param2)
foo(1,2,3,4,5)


#-----------------
def foo(runoob_1, runoob_2):
    print(runoob_1, runoob_2)
l = [1, 2]
foo(*l)


星号可以作为参数的解压来使用。