from data_structures.linear import Stack
from data_structures.trees import BinaryTree
import operator


def build_parse_tree(expression):
    expression = expression.split()
    tree_stack = Stack()
    parse_tree = BinaryTree('')

    tree_stack.push(parse_tree)
    current_tree = parse_tree

    for token in expression:
        if token == '(':
            current_tree.insert_left('')
            tree_stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif token not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_value(int(token))
            parent = tree_stack.pop()
            current_tree = parent
        elif token in ['+', '-', '*', '/']:
            current_tree.set_root_value(token)
            current_tree.insert_right('')
            tree_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif token == ')':
            current_tree = tree_stack.pop()
        else:
            raise ValueError

    return parse_tree


def evaluate_parse_tree(parse_tree):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()

    if left_child and right_child:
        function = operators[parse_tree.get_root_value()]
        return function(evaluate_parse_tree(left_child), evaluate_parse_tree(right_child))
    else:
        return parse_tree.get_root_value()


if __name__ == '__main__':
    expression = "( ( 10 + 5 ) * 3 )"

    print "Building parse tree for {}".format(expression)
    tree = build_parse_tree(expression)

    print "Evaluating parse tree for {}".format(expression)
    print "Value: {}".format(evaluate_parse_tree(tree))
