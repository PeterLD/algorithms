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
