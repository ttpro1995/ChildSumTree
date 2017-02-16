from node import Node

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

def make_data_tree2():

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
    ccc2 = Node(6)
    ccc3 = Node(7)
    ccc4 = Node(8)
    ccc5 = Node(5)
    ccc6 = Node(11)
    ccc7 = Node(12)
    ccc8 = Node(15)
    cc1.add_children([ccc1,ccc2])
    cc2.add_children([ccc3, ccc4])
    cc3.add_children([ccc5, ccc6])
    cc4.add_children([ccc7, ccc8])
    return root
