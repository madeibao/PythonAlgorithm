import os
import ast
import spacy  # 工业级别的应用用来解析句子。
import numpy as np
from errno import ENOENT
from collections import Counter

nlp = spacy.load('en_core_web_sm')  # 加载内核, 工业级别的应用内容。
 
doc = nlp("The big grey dog ate all of the chocolate,but fortunately he wasn't sick!")
 
​