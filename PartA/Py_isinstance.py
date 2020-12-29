arg=123
isinstance(arg, int)    #输出True
isinstance(arg, str)    #输出False
isinstance(arg, string) #报错



isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。
如果要判断两个类型是否相同推荐使用 isinstance()。
















