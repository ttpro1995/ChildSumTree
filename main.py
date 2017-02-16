from child_sum_tree import ChildSumTree
import make_tree


if __name__ == "__main__":
    tree_model = ChildSumTree()
    tree = make_tree.make_data_tree()
    traversal = tree_model._traversal_tree(tree)
    result = tree_model.compute_tree(tree)

    print ('tree 1')
    print ('traversal = ',traversal)
    print ('result = ',result)

    tree2 = make_tree.make_data_tree2()
    traversal2 = tree_model._traversal_tree(tree2)
    result2 = tree_model.compute_tree(tree2)
    print ('tree 2')
    print ('traversal 2 = ', traversal2)
    print ('result 2 = ', result2)

