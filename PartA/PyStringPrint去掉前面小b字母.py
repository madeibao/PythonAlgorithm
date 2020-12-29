
inputfile = './train.txt'

"""

train.txt里面的文件按照以下的格式进行存储。

I have to say they have one of the fastest $T$ in the city .
delivery times
1
 $T$ is always fresh and hot- ready to eat !
Food
1
Did I mention that the $T$ is OUTSTANDING ?
coffee
1


"""

lines = open(inputfile, "r", encoding='UTF-8').readlines()  # 每次读取其中的一行的单词.

for i in range(0, len(lines), 3):
      # words = lines[i].encode().lower().split()    					# 第一种打印格式如果时按照这种格式进行打印，
 	words = str(lines[i].encode().lower(), 'utf-8').split()			# 第二种打印格式。
    print(words)



"""
2019.7.24 				7：30PM


第一种打印出的结果为，结果每个字符前面都会有一个字符b

[b'the', b'$t$', b'is', b'top', b'notch', b'as', b'well', b'.']
[b'i', b'have', b'to', b'say', b'they', b'have', b'one', b'of', b'the', b'fastest', b'$t$', b'in', b'the', b'city', b'.']
[b'$t$', b'is', b'always', b'fresh', b'and', b'hot-', b'ready', b'to', b'eat', b'!']


第二种的打印的结果为：  这次变成了正常的结果。

['the', '$t$', 'is', 'top', 'notch', 'as', 'well', '.']
['i', 'have', 'to', 'say', 'they', 'have', 'one', 'of', 'the', 'fastest', '$t$', 'in', 'the', 'city', '.']
['$t$', 'is', 'always', 'fresh', 'and', 'hot-', 'ready', 'to', 'eat', '!']

"""

