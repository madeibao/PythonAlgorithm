import os
import unicodedata
import xml.etree.ElementTree as ET
from errno import ENOENT


input_fname = 'F:/pythonWorkSpace/IAN/data/restaurant/test.xml'       # 输入文件
output_fname = 'F:/pythonWorkSpace/IAN/data/restaurant/test.txt'      # 输出文件

if not os.path.isfile(input_fname):
    raise IOError(ENOENT, 'Not an input file', input_fname)
    
with open(output_fname, 'w') as f:  # 依照写的方式进行打开。
    tree = ET.parse(input_fname)
    root = tree.getroot()  # 获得根节点。
    sentence_num = 0
    aspect_num = 0
    for sentence in root.iter('sentence'):
        sentence_num = sentence_num + 1      # 句子的总数加一。
        text = sentence.find('text').text    # 一个句子里面的获取文本数据。
        for asp_terms in sentence.iter('aspectTerms'):
            for asp_term in asp_terms.findall('aspectTerm'):  # 一个句子中可能包含有多个术语。
                if asp_term.get('polarity') != 'conflict' and asp_term.get('target') != 'NULL':  # 术语的极性不冲突，并且术语目标不为空。
                    aspect_num = aspect_num + 1  # 方面词汇术语加一。
                    new_text = ''.join((text[:int(asp_term.get('from'))], 'aspect_term', text[int(asp_term.get('to')):]))
                    f.write('%s\n' % new_text.strip())
                    f.write('%s\n' % asp_term.get('term'))
                    f.write('%s\n' % asp_term.get('polarity'))
                    print("Read %s sentences %s aspects" % (sentence_num, aspect_num))






