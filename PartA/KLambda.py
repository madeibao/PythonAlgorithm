1、详见keras Lambda 层

keras.layers.core.Lambda(function, output_shape=None, mask=None, arguments=None)




function：要实现的函数，该函数仅接受一个变量，即上一层的输出，若要传入其余参数，需使用arguments参数。

output_shape：函数应该返回的值的shape，可以是一个tuple，也可以是一个根据输入shape计算输出shape的函数
所以，output_shape可以是一个函数，可以根据输入shape，计算输出shape的函数。

mask: 掩膜

arguments：可选，字典，用来记录向函数中传递的其他关键字参数








