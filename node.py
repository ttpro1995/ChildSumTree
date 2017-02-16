class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_children(self, nodes):
        self.children.extend(nodes)

    def has_child(self):
        if len(self.children) > 0:
            return True
        else:
            return False

    def has_both_child(self):
        if len(self.children) ==2:
            return True
        else:
            return False