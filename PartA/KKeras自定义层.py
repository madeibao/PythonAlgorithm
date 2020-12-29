class Layer(object):
#抽象类主要方法总结
 
  #为layer增加权重
  def add_weight()
  
  #对输入数据和本Layer定义的数据进行效验，如输入数据不符合定义规定报错
  def assert_input_compatibility(self, inputs):
 
  #训练过程中前向和后向传播的主要逻辑实现
  def call()
 
  #计算本层的输出形状
  def compute_output_shape()
 
  #计算输出的掩膜
  def compute_mask()
 
  #构造layer的权重
  def build()
 
  #检索给定节点上的层的输入\出形状
  def get_input_shape_at()
  def get_output_shape_at()
 
  #检索给定节点上的层的输入/出张量
  def get_input_at():
  def get_output_at():
 
  #检索给定节点上的层的输入/出掩模张量。
  def get_input_mask_at(self, node_index):
  def get_output_mask_at(self, node_index):