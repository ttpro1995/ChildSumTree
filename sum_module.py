import theano
import theano.tensor as T
import numpy as np

class ChildSumModule():
    """
    Sum value of two child and its value
    """
    def __init__(self):
        self.W = theano.shared(1,name='W')

    def get_recursive_module(self, child_h):
        # internal_h = node val + h of children
        cur_val = T.lscalar('val')
        child_h_sum = T.sum(child_h, axis=0)
        h = T.dot(child_h_sum, self.W) + cur_val
        return (cur_val, h)

    def get_leaf_module(self):
        # for leaf node (without any children)
        # leaf h = its val
        cur_val = T.lscalar('val')
        h =  cur_val
        return (cur_val, h)






