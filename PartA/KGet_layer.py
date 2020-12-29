
【题目】keras中获取层输出shape的方法汇总



在keras 中，要想获取层输出shape，可以先获取层对象，再通过层对象的属性output或者output_shape获得层输出shape(若要获取层输入shape,可以用input/input_shape)。两者的输出分别为：
output: (红框部分分别表示层名以及输出shape)
output_shape:(即为层输出shape）
获取层对象的方法有两种，一种是使用model.get_layer()方法，另一种是使用model.layers[index]。
当然，你也可以使用model.summary（）打印出整个模型，从而可以获取层输出shape。
