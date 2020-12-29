import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.recurrent import SimpleRNN
from keras.optimizers import Adam

inputs_size = 28
time_steps = 28
cell_size = 50

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train/255.0
x_test = x_test/255.0

y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)


model = Sequential()

model.add(SimpleRNN(
    units=cell_size,
    input_shape=(time_steps, inputs_size),
))

model.add(Dense(10, activation='softmax'))
adam = Adam(lr=1e-4)
model.compile(optimizer=adam, loss='categorical_crossentropy',  metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=54, epochs=10)
loss, accuracy = model.evaluate(x_test, y_test)

print('test loss',loss)
print('test accuracy',accuracy)







