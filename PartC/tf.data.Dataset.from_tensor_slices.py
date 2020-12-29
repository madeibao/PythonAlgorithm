dataset = tf.data.Dataset.from_tensor_slices(np.random.uniform(size=(5, 2))) 
传入的数值是一个矩阵，它的形状为(5, 2)，tf.data.Dataset.from_tensor_slices就会切分它形状上的第一个维度，
最后生成的dataset中一个含有5个元素，每个元素的形状是(2, )，即每个元素是矩阵的一行。