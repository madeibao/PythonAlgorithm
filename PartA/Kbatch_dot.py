import keras.backend as K
import numpy as np

w = K.variable(np.random.randint(10, size=(10, 12, 4, 5)))
k = K.variable(np.random.randint(10, size=(10, 12, 5, 8)))
z = K.batch_dot(w, k)
print(z.shape)   # (10, 12, 4, 8)










