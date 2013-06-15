class BinaryTree:
    def __init__(self, root_object):
        self.key = root_object
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child:
            new_tree = BinaryTree(new_node)
            new_tree.left_child = self.left_child
            self.left_child = new_tree
        else:
            self.left_child = BinaryTree(new_node)

    def insert_right(self, new_node):
        if self.right_child:
            new_tree = BinaryTree(new_node)
            new_tree.right_child = self.right_child
            self.right_child = new_tree
        else:
            self.right_child = BinaryTree(new_node)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, new_object):
        self.key = new_object

    def get_root_value(self):
        return self.key
