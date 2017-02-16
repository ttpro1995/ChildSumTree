from sum_module import ChildSumModule
from node import Node
import theano

builder = ChildSumModule()

def make_data_tree():
    root = Node(3)
    c1 = Node(5)
    c2 = Node(7)
    cc1 = Node(10)
    cc2 = Node(12)
    cc3 = Node(9)
    cc4 = Node(8)
    root.add_children([c1,c2])
    c1.add_children([cc1,cc2])
    c2.add_children([cc3,cc4])
    ccc1 = Node(2)
    ccc3 = Node(6)
    cc2.add_children([ccc1,ccc3])
    return root

def test_module_one_cell():
    # this is just one cell
    child_val, cur_val, h = ChildSumModule().get_module()
    f = theano.function([child_val, cur_val], h, allow_input_downcast=True)
    result = f([3,4], 5) # (3+4)*5
    print (result)

def make_simple_tree():
    root = Node(3)
    c1 = Node(5)
    c2 = Node(7)
    root.add_children([c1,c2])
    return root

def build_computation_graph_manually():
    builder = ChildSumModule()
    # c1
    c1_child, c1_val, c1_h = builder.get_leaf_module()
    # c2
    c2_child, c2_val, c2_h = builder.get_leaf_module()
    # root
    root_val, root_h = builder.get_recursive_module([c1_h, c2_h])

    f = theano.function([c1_child, c2_child, c1_val, c2_val, root_val], root_h, allow_input_downcast=True, on_unused_input='ignore')
    f_sub = theano.function([c1_child,c1_val], c1_h, allow_input_downcast=True)

    child_dummy = [1,2]
    result = f(child_dummy, child_dummy, 5, 7, 3)
    result_sub = f_sub(child_dummy, 5)
    print (result)
    print (result_sub)

list_child = []
list_val = []
list_h = []

def build_computation_graph_auto(root):
    if (root.has_both_child()): # node with child
        child_h_1 = build_computation_graph_auto(root.children[0])
        child_h_2 = build_computation_graph_auto(root.children[1])
        node_val, node_h = build_graph_cell(root, child_h_1, child_h_2)
        list_val.append(node_val)
        list_h.append(node_h)
        return node_h
    else: # leaf node
        node_child, node_val, node_h = build_graph_cell(root, None, None)
        list_child.append(node_child)
        list_val.append(node_val)
        list_h.append(node_h)
        return node_h

def build_graph_cell(node, c1_h, c2_h):
    node_child = Node
    if c1_h == None:
        node_child, node_val, node_h = builder.get_leaf_module()
        return node_child, node_val, node_h
    else:
        node_val, node_h = builder.get_recursive_module([c1_h, c2_h])
    return node_val, node_h

traversal_val = []
def traversal(root):
    if (root.has_both_child()):
        traversal(root.children[0])
        traversal_val.append(root.val)
        traversal(root.children[1])
    else:
        traversal_val.append(root.val)


if __name__ == "__main__":
    # test_module_one_cell()
    # build_computation_graph_manually()
    tree = make_data_tree()
    build_computation_graph_auto(tree)
    inps = []
    inps.extend(list_child)
    inps.extend(list_val)
    outputs = []
    outputs.extend(list_h)
    traversal(tree)
    f = theano.function(inps, outputs, allow_input_downcast=True)
    dummy_child = [0,0]
    dummy_children = []
    for i in range(0, len(list_child)):
        dummy_children.append(dummy_child)
    input_seq = dummy_children+traversal_val
    result = f(*input_seq)
    print (result)