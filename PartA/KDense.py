# coding:utf-8
from keras.models import Input, Model
from keras.layers import Dense


x = Input(shape=(32,))
y = Dense(16, activation='softmax')(x)
model = Model(x, y)


print(model.summary())





_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         (None, 32)                0         
_________________________________________________________________
dense_1 (Dense)              (None, 16)                528           全连接层的参数设置，32*16+16=528个参数。
=================================================================
Total params: 528
Trainable params: 528
Non-trainable params: 0
_________________________________________________________________
None

