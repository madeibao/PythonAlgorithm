
# -*- coding:UTF-8 -*-

inputfile = './train.txt'
target_words = []
y = []

lines = open(inputfile, encoding='UTF-8').readlines()  # 每次读取其中的一行的单词.
for i in range(0, len(lines), 3):
    y.append(lines[i + 2].strip().split()[0])
    words = lines[i].decode(encoding='UTF-8').lower().split()
    print(words)




"""

这种适合python2.7的版本，正确的使用2.7版本能够运行成功，得出如下的结果。


['the', '$t$', 'is', 'top', 'notch', 'as', 'well', '.']
['i', 'have', 'to', 'say', 'they', 'have', 'one', 'of', 'the', 'fastest', '$t$', 'in', 'the', 'city', '.']
['$t$', 'is', 'always', 'fresh', 'and', 'hot-', 'ready', 'to', 'eat', '!']
['did', 'i', 'mention', 'that', 'the', '$t$', 'is', 'outstanding', '?']
['certainly', 'not', 'the', 'best', 'sushi', 'in', 'new', 'york', ',', 'however', ',', 'it', 'is', 'always', 'fresh', ',', 'and', 'the', '$t$', 'is', 'very', 'clean', ',', 'sterile', '.']
['i', 'trust', 'the', '$t$', 'at', 'go', 'sushi', ',', 'it', 'never', 'disappoints', '.']
['straight-forward', ',', 'no', 'surprises', ',', 'very', 'decent', '$t$', '.']
['best', 'spicy', '2', 'tuna', 'roll', ',', 'great', '$t$', '.']
['best', '$t$', ',', 'great', 'asian', 'salad', '.']
['try', 'the', '$t$', '(', 'not', 'on', 'menu', ')', '.']
['try', 'the', 'rose', 'roll', '(', 'not', 'on', '$t$', ')', '.']

"""