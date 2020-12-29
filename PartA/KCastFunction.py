
from keras import backend as K
input = K.placeholder((2, 3), dtype='float32')
print(K.cast(input, dtype='float16'))





















