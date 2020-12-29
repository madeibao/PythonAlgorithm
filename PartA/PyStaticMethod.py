class C(object):
    @staticmethod
    def f():
        print('runoob')


C.f()  # 静态方法无需实例化
cobj = C()
cobj.f()




# 输出结果为：
# runoob
# runoob

