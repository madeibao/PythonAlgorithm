
import nltk
from nltk import data
data.path.append(r"D:/BaiduNetdiskDownload/nltk_data")   # 这里的路径需要换成自己数据文件下载的路径 
# 以上的方法是一个通用的方法，十分的有效。



text = 'PathonTip.com is a very good website. We can learn a lot from it.'
#将文本拆分成句子列表
sens = nltk.sent_tokenize(text)
print(sens)
#将句子进行分词,nltk的分词是句子级的,因此要先分句,再逐句分词,否则效果会很差.
words = []
for sent in sens:
    words.append(nltk.word_tokenize(sent))
print(words)





