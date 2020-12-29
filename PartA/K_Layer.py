class Layer(object):
    def __init__(self, **kwargs):
     
    @staticmethod
    def _node_key(layer, node_index):
 
    @property
    def losses(self):
    
    @property
    def updates(self):
      
    @property
    def built(self):
       
    @built.setter
    def built(self, value):
   
    @property
    def trainable_weights(self):
 
    @trainable_weights.setter
    def trainable_weights(self, weights):
    
    @property
    def non_trainable_weights(self):
      
    @non_trainable_weights.setter
    def non_trainable_weights(self, weights):
 
    @interfaces.legacy_add_weight_support
    def add_weight(self,name,shape,dtype=None,initializer=None,regularizer=None,
                   trainable=True,
                   constraint=None):
     
    def assert_input_compatibility(self, inputs):
       
    def call(self, inputs, **kwargs):
      
    def __call__(self, inputs, **kwargs):
 
    def _add_inbound_node(self, input_tensors, output_tensors,
                          input_masks, output_masks,
                          input_shapes, output_shapes, arguments=None):
 
    def compute_output_shape(self, input_shape):
     
    def compute_mask(self, inputs, mask=None):
 
    def _get_node_attribute_at_index(self, node_index, attr, attr_name):
 
    def get_input_shape_at(self, node_index):
 
    def get_output_shape_at(self, node_index):
       
    def get_input_at(self, node_index):
       
    def get_output_at(self, node_index):
 
    def get_input_mask_at(self, node_index):
      
    def get_output_mask_at(self, node_index):
       
    @property
    def input(self):
 
    @property
    def output(self):
 
    @property
    def input_mask(self):
 
    @property
    def output_mask(self):
        
    @property
    def input_shape(self):
       
    @property
    def output_shape(self):
 
    def add_loss(self, losses, inputs=None):
 
    def add_update(self, updates, inputs=None):
 
    def get_updates_for(self, inputs):
       
    def get_losses_for(self, inputs):
 
    @property
    def weights(self):
 
    def set_weights(self, weights):
       
    def get_weights(self):
       
    def get_config(self):
        
    @classmethod
    def from_config(cls, config):
 
    def count_params(self):