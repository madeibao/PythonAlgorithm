


def singleton(cls):
    instances = {}
    def getinstance(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)
        return instances[cls]
    return getinstance

@singleton
class ClassA:
    pass

@singleton
class ClassB:
    pass

class ClassC:
    pass

aa=ClassA()
aaa=ClassA()

bb=ClassB()
bbb=ClassB()

cc=ClassC()
ccc=ClassC()


print(id(aa))
print(id(aaa))

print(id(bb))
print(id(bbb))

print(id(cc))
print(id(ccc))




