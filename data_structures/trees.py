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


class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_up(self, node_position):
        while node_position // 2 > 0:
            if self.heap_list[node_position] < self.heap_list[node_position // 2]:
                self.heap_list[node_position], self.heap_list[node_position // 2] = self.heap_list[node_position // 2], self.heap_list[node_position]
            node_position = node_position // 2

    def pop_min(self):
        min_value = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)

        return min_value

    def perc_down(self, node_position):
        while node_position * 2 <= self.current_size:
            min_child = self.min_child(node_position)

            if self.heap_list[node_position] > self.heap_list[min_child]:
                self.heap_list[node_position], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[node_position]

            node_position = min_child

    def min_child(self, node_position):
        if node_position * 2 + 1 > self.current_size:
            return node_position * 2
        else:
            if self.heap_list[node_position * 2] < self.heap_list[node_position * 2 + 1]:
                return node_position * 2
            else:
                return node_position * 2 + 1

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]

        while (i > 0):
            self.perc_down(i)
            i = i - 1


class MaxHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_up(self, node_position):
        while node_position // 2 > 0:
            if self.heap_list[node_position] > self.heap_list[node_position // 2]:
                self.heap_list[node_position], self.heap_list[node_position // 2] = self.heap_list[node_position // 2], self.heap_list[node_position]
            node_position = node_position // 2

    def pop_max(self):
        max_value = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)

        return max_value

    def perc_down(self, node_position):
        while node_position * 2 <= self.current_size:
            max_child = self.max_child(node_position)

            if self.heap_list[node_position] < self.heap_list[max_child]:
                self.heap_list[node_position], self.heap_list[max_child] = self.heap_list[max_child], self.heap_list[node_position]

            node_position = max_child

    def max_child(self, node_position):
        if node_position * 2 + 1 > self.current_size:
            return node_position * 2
        else:
            if self.heap_list[node_position * 2] > self.heap_list[node_position * 2 + 1]:
                return node_position * 2
            else:
                return node_position * 2 + 1

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list

        while i > 0:
            self.perc_down(i)
            i = i - 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __repr__(self):
        return str([(key, self[key]) for key in self])

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)

        self.size = self.size + 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
        elif key > current_node.key:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
        else:
            current_node.replace_node_data(key, value, current_node.left_child, current_node.right_child)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)

            if result:
                return result.payload
            else:
                return None

        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif key == current_node.key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)

            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Key "{}" not in tree'.format(key))
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Key "{}" not in tree'.format(key))

    def remove(self, node_to_remove):
        if node_to_remove.is_leaf():
            if node_to_remove == node_to_remove.parent.left_child:
                node_to_remove.parent.left_child = None
            else:
                node_to_remove.parent.right_child = None

        elif node_to_remove.has_both_children():
            successor = node_to_remove.find_successor()
            successor.splice_out()

            node_to_remove.key = successor.key
            node_to_remove.payload = successor.payload

        else:
            if node_to_remove.has_left_child():
                if node_to_remove.is_left_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.left_child = node_to_remove.left_child
                elif node_to_remove.is_right_child():
                    node_to_remove.left_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.left_child
                else:
                    node_to_remove.replace_node_data(node_to_remove.left_child.key,
                        node_to_remove.left_child.payload,
                        node_to_remove.left_child.left_child,
                        node_to_remove.left_child.right_child)

            else:
                if node_to_remove.is_left_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.left_child = node_to_remove.right_child
                elif node_to_remove.is_right_child():
                    node_to_remove.right_child.parent = node_to_remove.parent
                    node_to_remove.parent.right_child = node_to_remove.right_child
                else:
                    node_to_remove.replace_node_data(node_to_remove.right_child.key,
                        node_to_remove.right_child.payload,
                        node_to_remove.right_child.left_child.
                        node_to_remove.right_child.right_child)

    def __delitem__(self, key):
        self.delete(key)


class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def find_successor(self):
        successor = None

        if self.has_right_child():
            successor = self.right_child.find_min()

        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self

        return successor

    def find_min(self):
        current_node = self

        while current_node.has_left_child():
            current_node = current_node.left_child

        return current_node

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child

                self.left_child.parent = self.parent

            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child

                self.right_child.parent = self.parent

    def replace_node_data(self, key, value, left_child, right_child):
        self.key = key
        self.payload = value
        self.left_child = left_child
        self.right_child = right_child
        if self.has_right_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def __iter__(self):
        if self:
            if self.has_left_child():
                for node in self.left_child:
                    yield node

            yield self.key

            if self.has_right_child():
                for node in self.right_child:
                    yield node
