embeddings_index = {}
glove1 = './resource/glove.6B.100d.txt'
f = open(glove1,'r')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()
 
print('Found %s word vectors.' % len(embeddings_index))













