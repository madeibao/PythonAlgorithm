关于保存h5模型、权重网上的示例非常多，也非常简单。主要有以下两个函数：
1、keras.models.load_model() 读取网络、权重
2、keras.models.load_weights() 仅读取权重
load_model代码包含load_weights的代码，区别在于load_weights时需要先有网络、并且load_weights需要将权重数据写入到对应网络层的tensor中。
