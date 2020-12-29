


tf.nn.conv2d (input, filter, strides, padding, use_cudnn_on_gpu=None, data_format=None, name=None)

参数：


参数：
input : 输入的要做卷积的图片，要求为一个张量，
shape为 [ batch, in_height, in_width, in_channel ]，
其中batch为图片的数量，in_height 为图片高度，in_width 为图片宽度，in_channel 为图片的通道数，灰度图该值为1，彩色图为3。
（也可以用其它值，但是具体含义不是很理解）



filter： 卷积核，要求也是一个张量，shape为 [ filter_height, filter_width, in_channel, out_channels ]，
其中 filter_height 为卷积核高度，filter_width 为卷积核宽度，in_channel 是图像通道数 ，和 input 的 in_channel 要保持一致，out_channel 是卷积核数量。


strides： 卷积时在图像每一维的步长，这是一个一维的向量，[ 1, strides, strides, 1]，第一位和最后一位固定必须是1


padding： string类型，值为“SAME” 和 “VALID”，表示的是卷积的形式，是否考虑边界。"SAME"是考虑边界，不足的时候用0去填充周围，"VALID"则不考虑
use_cudnn_on_gpu： bool类型，是否使用cudnn加速，默认为true