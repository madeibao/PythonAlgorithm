


word2id = {}

words = ['I','am','a','student','hello','word','school','school','Ni','tom','java','python','they']
for i in words:
	if i not in word2id:
		word2id[i]=len(word2id)

print(word2id)  # 把列表的形式写成字典的形式进行存储。




# 结果为如图所示。
# {'python': 10, 'Ni': 7, 'hello': 4, 'am': 1, 'tom': 8, 'they': 11, 'school': 6, 'student': 3, 'java': 9, 'word': 5, 'I': 0, 'a': 2}






