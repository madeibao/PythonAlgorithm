
logger：日志对象，logging模块中最基础的对象，

用logging.getLogger(name)方法进行初始化，name可以不填。通常logger的名字我们对应模块名，如聊天模块、数据库模块、验证模块等。



logger = logging.getLogger()   # 写入日志的文件。
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

setLevel()：设置日志等级
日志等级分别有以下几种：
CRITICAL : 'CRITICAL',
ERROR : 'ERROR',
WARNING : 'WARNING',
INFO : 'INFO',
DEBUG : 'DEBUG',
NOTSET : 'NOTSET',




1.等级排序：
   debug < info < warn < error < fatal
2.各等级的含义：
  1.debug: 级别最低，用户开发过程中的调试
  2.info：打印程序运行是的正常的信息，用于替代print输出
  3.warn: 打印警告信息，不影响程序的运行
  4.error: 程序运行出错，可以修复，常用在except异常捕获之后
  5.fatal：非常严重，无法修复，程序继续运行的话后果非常严重




# 训练的内容表示情况。
logger.info('> training arguments:')


#=================================================================
#-----------------------------------------------------------------

import logging 

# 1、创建一个logger 
logger = logging.getLogger('mylogger') 
logger.setLevel(logging.DEBUG) 

# 2、创建一个handler，用于写入日志文件 
fh = logging.FileHandler('test.log') 
fh.setLevel(logging.DEBUG) 

# 再创建一个handler，用于输出到控制台 
ch = logging.StreamHandler() 
ch.setLevel(logging.DEBUG) 

# 3、定义handler的输出格式（formatter）
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 

# 4、给handler添加formatter
fh.setFormatter(formatter) 
ch.setFormatter(formatter) 

# 5、给logger添加handler 
logger.addHandler(fh) 
logger.addHandler(ch)


