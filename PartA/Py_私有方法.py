
class Test(object):
    #普通方法

    def test(self):

        print("普通方法test")

    #普通方法

    def _test1(self):

        print("普通方法_test1方法")

    #私有方法

    def __test2(self):

        print("私有方法__test2方法")

 

t = Test()

t.test()

t._test1()

#t.__test2()#调用的时候会报错





