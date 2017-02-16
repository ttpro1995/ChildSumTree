from sum_module import ChildSumModule
import theano

class ChildSumTree:
    def __init__(self):
        self.builder = ChildSumModule()
        self.tree = None

    def _build_graph(self,tree):
        """
        Build computation graph
        :param tree: root node of the tree
        :return:
        """
        list_val = [] # input of computation graph
        list_h = [] # output of computation graph
        def build_cell(node, children_h):
            if (node.has_child()):
                assert len(children_h) > 0
                val, h = self.builder.get_recursive_module(children_h)
            else:
                val, h = self.builder.get_leaf_module()
            return val, h

        def recursive_build_graph(node):
            if(node.has_child()):
                h_1 = recursive_build_graph(node.children[0])
                h_2 = recursive_build_graph(node.children[1])
                input_val, h = build_cell(node, [h_1, h_2])
            else:
                input_val, h = build_cell(node, None)
            list_val.append(input_val)
            list_h.append(h)
            return h

        recursive_build_graph(tree)
        return list_val, list_h

    def _traversal_tree(self, tree):
        list_val = []
        def traversal_recursive(tree):
            if (tree.has_child()):
                traversal_recursive(tree.children[0])
                traversal_recursive(tree.children[1])
                val = tree.val
                list_val.append(val)
            else:
                list_val.append(tree.val)

        traversal_recursive(tree)
        return list_val

    def compute_tree(self, tree):
        """
        Compute h of every node giving a tree
        """
        g_list_val, g_list_h = self._build_graph(tree)
        list_val = self._traversal_tree(tree)
        f = theano.function(g_list_val, g_list_h, allow_input_downcast=True)
        result = f(*list_val)
        return result