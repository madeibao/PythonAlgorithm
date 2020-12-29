



pickle.dump(obj, file, protocol=None,)
必填参数obj表示将要封装的对象
必填参数file表示obj要写入的文件对象，file必须以二进制可写模式打开，即“wb”
可选参数protocol表示告知pickler使用的协议，支持的协议有0,1,2,3，默认的协议是添加在Python 3中的协议3。　　　
dump 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
with open('D:/tmp.pk', 'w') as f:
pickle.dump(data, f)
pickle.load(file,*,fix_imports=True, encoding="ASCII", errors="strict")
必填参数file必须以二进制可读模式打开，即“rb”，其他都为可选参数
load 从数据文件中读取数据，并转换为python的数据结构



with open('D:/tmp.pk', 'r') as f:
data = pickle.load(f)
pickle.dumps(obj)：以字节对象形式返回封装的对象，不需要写入文件中
pickle.loads(bytes_object): 从字节对象中读取被封装的对象，并返回



pickle模块可能出现三种异常：
PickleError：封装和拆封时出现的异常类，继承自Exception
PicklingError: 遇到不可封装的对象时出现的异常，继承自PickleError
UnPicklingError: 拆封对象过程中出现的异常，继承自PickleError


