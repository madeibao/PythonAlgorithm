import spacy
from collections import Counter

save_fname = './data_info2.txt'

word2id = {}     # 创建一个空的字典。
words = ['but', 'the', 'aspect_term', 'was', 'so', 'horrible', 'to', 'us', '.', 'to', 'be', 'completely', 'fair', ',', 'the', 'only', 'redeeming', 'factor', 'was', 'the', 'aspect_term', ',', 'which', 'was', 'above', 'average', ',', 'but', 'could', "n't", 'make', 'up', 'for', 'all', 'the', 'other', 'deficiencies', 'of', 'teodora', '.', 'the', 'aspect_term', 'is', 'uniformly', 'exceptional', ',', 'with', 'a', 'very', 'capable', 'kitchen', 'which', 'will', 'proudly', 'whip', 'up', 'whatever', 'you', 'feel', 'like', 'eating', ',', 'whether', 'it', "'s", 'on', 'the', 'menu', 'or', 'not', '.', 'the', 'food', 'is', 'uniformly', 'exceptional', ',', 'with', 'a', 'very', 'capable', 'aspect_term', 'which', 'will', 'proudly', 'whip', 'up', 'whatever', 'you', 'feel', 'like', 'eating', ',', 'whether', 'it', "'s", 'on', 'the', 'menu', 'or', 'not', '.', 'the', 'food', 'is', 'uniformly', 'exceptional', ',', 'with', 'a', 'very', 'capable', 'kitchen', 'which', 'will', 'proudly', 'whip', 'up', 'whatever', 'you', 'feel', 'like', 'eating', ',', 'whether', 'it', "'s", 'on', 'the', 'aspect_term', 'or', 'not', '.', 'not', 'only', 'was', 'the', 'aspect_term', 'outstanding', ',', 'but', 'the', 'little', "'", 'perks', "'", 'were', 'great', '.', 'not', 'only', 'was', 'the', 'food', 'outstanding', ',', 'but', 'the', 'little', "'", 'aspect_term', "'", 'were', 'great', '.']

word_count = Counter(words).most_common()   # 计算单词的数量。返回列表中的所有的元素，如果元素是相同的，则排序是无关的。
print(word_count)
print("----------------------------------------------------------------------------------------")
for word, _ in word_count:
    if word == ' ':
        print('haha')
    if word not in word2id and ' ' not in word and '\n' not in word and 'aspect_term' not in word:
        word2id[word] = len(word2id)
print(word2id)

with open(save_fname, 'w') as f:  # 保存的实验模型中。
    for key, value in word2id.items():
        f.write('%s %s\n' % (key, value))  #写入字典。  中间还有一个空格。

