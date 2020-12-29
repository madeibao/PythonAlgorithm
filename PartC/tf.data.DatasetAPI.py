从内存中创建更复杂的Dataset
tf.data.Dataset.from_tensor_slices真正的作用是切分传入Tensor的第一个维度，生成相应的dataset。例如：



dataset = tf.data.Dataset.from_tensor_slices(np.random.uniform(size=(5, 2)))
