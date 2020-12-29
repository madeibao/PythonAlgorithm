seed（）函数是用来控制生成有规律随机数的。seed（）函数是用来控制生成有规律随机数的。seed（）函数是用来控制生成有规律随机数的。


	当（）中有数值时，生成与该值相关的随机数
	
import numpy as np


例如， 当（）中的值为0时，
np.random.seed(0)
print(np.random.randn(1, 3))
np.random.seed(0)
print(np.random.randn(1, 3))

[[1.76405235 0.40015721 0.97873798]]
[[1.76405235 0.40015721 0.97873798]]

当（）中的值为1时，
np.random.seed(1)
print(np.random.randn(1, 3))
np.random.seed(1)
print(np.random.randn(1, 3))

[[ 1.62434536 -0.61175641 -0.52817175]]
[[ 1.62434536 -0.61175641 -0.52817175]]

（）中的值固定时，对应生成的随机数是固定不变的，例如，当（）中的数为0时，生成的1*3矩阵只有一种，即

[[1.76405235 0.40015721 0.97873798]]

值得注意的是，seed()的效果只有一次，即只对seed()之后离其最近的代码 np.random.randn(1, 3) 起作用，例如

np.random.seed(0)
print(np.random.randn(1, 3))
print(np.random.randn(1, 3))

[[1.76405235 0.40015721 0.97873798]]
[[ 2.2408932   1.86755799 -0.97727788]]

可以看出，np.random.seed(0)对第二段代码 np.random.randn(1, 3) 没作用

  2. 当（）中没有数值时，生成与该值无关的随机数

np.random.seed()
print(np.random.randn(1, 3))
print(np.random.randn(1, 3))

[[ 0.42128832 -0.95154595 -1.11228585]][[-0.16132993 -0.59064208 -0.32277392]]
