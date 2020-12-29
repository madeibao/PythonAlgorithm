
import os
import pickle   # 此模块能够将训练的模型保存在磁盘里面。
import numpy as np
import tensorflow as tf
import keras.preprocessing.text as T
from keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences


max_length = 10
text1 = 'some thing to eat'
text2 = 'some thing to drink'
text3 = 'some thing men and me'
texts = [text1, text2, text3]

print(T.text_to_word_sequence(text1))    # 以空格区分，中文也不例外 ['some', 'thing', 'to', 'eat']
tokenizer = Tokenizer(num_words=None)  # num_words:None或整数,处理的最大单词数量。少于此数的单词丢掉
tokenizer.fit_on_texts(texts)
print(tokenizer.word_counts)     # [('some', 2), ('thing', 2), ('to', 2), ('eat', 1), ('drink', 1)]
print(tokenizer.word_index)      # {'some': 1, 'thing': 2,'to': 3 ','eat': 4, drink': 5}
print(tokenizer.word_docs)       # {'some': 2, 'thing': 2, 'to': 2, 'drink': 1,  'eat': 1}
print(tokenizer.index_docs)      # {1: 2, 2: 2, 3: 2, 4: 1, 5: 1}


# num_words=多少会影响下面的结果，行数=num_words
text_to_sequences = tokenizer.texts_to_sequences(texts)
print(text_to_sequences)
# [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 6, 7, 8]]
text_to_sequences = pad_sequences(text_to_sequences, maxlen=max_length)   # 前向的填充的结果值。
print(text_to_sequences)
"""
填充之后的结果为：
[[0 0 0 0 0 0 1 2 3 4]
 [0 0 0 0 0 0 1 2 3 5]
 [0 0 0 0 0 1 2 6 7 8]]

"""
print(tokenizer.texts_to_matrix(texts))     # 矩阵化=one_hot   三个句子的矩阵化的操作。
'''
[[0. 1. 1. 1. 1. 0. 0. 0. 0.]
 [0. 1. 1. 1. 0. 1. 0. 0. 0.]
 [0. 1. 1. 0. 0. 0. 1. 1. 1.]]
'''
























