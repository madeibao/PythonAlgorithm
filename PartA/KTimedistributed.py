

from keras.models import Input,Model
from keras.layers import Dense,Conv2D,TimeDistributed
 
input_ = Input(shape=(12,8))
out = TimeDistributed(Dense(units=10))(input_)
#out = Dense(units=10)(input_)
model = Model(inputs=input_,outputs=out)
model.summary()



# 模型的结果如下所示:
# _________________________________________________________________
# Layer (type)                 Output Shape              Param #   
# =================================================================
# input_1 (InputLayer)         (None, 12, 8)             0         
# _________________________________________________________________
# time_distributed_1 (TimeDist (None, 12, 10)            90        
# =================================================================
# Total params: 90
# Trainable params: 90
# Non-trainable params: 0
# _________________________________________________________________