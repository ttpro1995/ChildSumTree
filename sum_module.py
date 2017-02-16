import theano
import theano.tensor as T
import numpy as np

class ChildSumModule():
    def __init__(self):
        self.W = theano.shared(1,name='W')

    def get_module(self):
        child_h = T.lvector('child_h')
        cur_val = T.lscalar('val')
        child_h_sum = T.sum(child_h, axis=0)
        h = T.dot(child_h_sum, self.W)  + cur_val
        return (child_h, cur_val, h)

    def get_recursive_module(self, child_h):
        cur_val = T.lscalar('val')
        child_h_sum = T.sum(child_h, axis=0)
        h = T.dot(child_h_sum, self.W) + cur_val
        return (cur_val, h)

    def get_leaf_module(self):
        return self.get_module()






