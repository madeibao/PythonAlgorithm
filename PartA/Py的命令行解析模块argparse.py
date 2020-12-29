Python模块学习 - Argparse 

argparse模块
　　在Python中，argparse模块是标准库中用来解析命令行参数的模块，
用来替代已经过时的optparse模块。argparse模块能够根据程序中的定义从sys.argv中解析出来这些参数，并自动生成帮助和使用信息。



#-------------------------------------------------------------------
#-------------------------------------------------------------------



使用argparse解析命令行参数时，首先需要创建一个解析器：
import argparse
 
parser = argparse.ArgumentParser()


add_argument:读入命令行参数，该调用有多个参数
ArgumentParser.add_argument(name or flags…[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])



name or flags:是必须的参数，该参数接受选项参数或者是位置参数（一串文件名）


比如说下面的这个结果值的内容。
parser.add_argument('--dataset', default='twitter', type=str, help='twitter, restaurant, laptop')



# 下面的语句就是返回一个命名空间内容。
opt = parser.parse_args()  #      #返回一个命名空间,如果想要使用变量,可用opt.attr
