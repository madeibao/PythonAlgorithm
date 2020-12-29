def convert_embedding_file():
    # 词向量中，第一个是单词，后面的是一个按照空格分割的300维度的向量。

    embedding_file = "./resource/glove.42B.300d.txt"  # 把训练好的词向量全都变成字典的形式来进行存储。
    rf = open(embedding_file, 'r', encoding='utf-8')  # 打开词向量文件。
    embeddings_index = {}  # 创建一个空的字典。
    print("reading embedding from " + embedding_file)  # 下面开始读取其中的文件内容。
    count = 0
    for line in rf:
        count += 1
        if count % 100000 == 0:  # 这里用来统计词嵌入矩阵的单词的数量。
            print(str(count))

        values = line.split()           # 每次分割300个元素的内容。  第一个存储的是的单词。意思就是每次只能够读取其中的一行的单词。
        index = len(values) - 300       # 一般是301-300 = 1,  所以一般的情况下是1.
        if len(values) > (300+ 1):      # 对于一些词嵌入的单词可能使得不只是一个单词组成，所以用下面的情况进行判断。
            word = ""  # 一个空的字符串。                 # 例如由  Bill Gates组成，，所以单词的长度会超过一般的情况。
            for i in range(len(values) - 300):
                word += values[i] + " "
            word = word.strip()  # 去除前后的空格。    # 去除前后的空格的部分内容。
        else:
            word = values[0]  # 单词是values[0]的形式。

        coefs = np.asarray(values[index:], dtype='float32')  # 作为矩阵存储其中的元素。  一个向量。从索引值后面的内容都是词向量的数字。
        embeddings_index[word] = coefs  # 把对应的内容用字典存储起来。
    rf.close()  # 关闭文件。
    print("finish.")  # 完成操作。


这里将glove的词向量转化成一个字典的形式来进行存储，
glove的词向量的存储的格式为
a 2323 23 2322 454 55 55 55 667 77 
b 2323 23 2322 454 55 55 55 667 77 
c 2323 23 2322 454 55 55 55 667 77
m n 2323 23 2322 454 55 55 55 667 77   

采用的是一个单词加上后面的后面的维度的数据，例如50维度或者是300维度的遗传数字。
但是可能存在着这种情况，就是一个词嵌入单词可能不只是由一个单词组成的情况。
这种情况下解析一行之后所得到的文件的长度要大于普通的情况,所以要进行判断是否是由一个单词组成，还是多个单词组成。

