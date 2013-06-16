from parse_tree import build_parse_tree
import operator


def preorder_traversal(tree):
    if tree:
        print(tree.get_root_value())
        preorder_traversal(tree.get_left_child())
        preorder_traversal(tree.get_right_child())


def inorder_traversal(tree):
    if tree:
        inorder_traversal(tree.get_left_child())
        print(tree.get_root_value())
        inorder_traversal(tree.get_right_child())


def postorder_traversal(tree):
    if tree:
        postorder_traversal(tree.get_left_child())
        postorder_traversal(tree.get_right_child())
        print(tree.get_root_value())


def postorder_evaluation(tree):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    result_1 = None
    result_2 = None

    if tree:
        result_1 = postorder_evaluation(tree.get_left_child())
        result_2 = postorder_evaluation(tree.get_right_child())

        if result_1 and result_2:
            return operators[tree.get_root_value()](result_1, result_2)
        else:
            return tree.get_root_value()


def print_expression(tree):
    string_value = ""

    if tree:
        string_value = "(" + print_expression(tree.get_left_child())
        string_value = string_value + str(tree.get_root_value())
        string_value = string_value + print_expression(tree.get_right_child()) + ")"

    return string_value


if __name__ == '__main__':
    expression = "( ( 10 + 5 ) * 3 )"

    print "Building parse tree for {}".format(expression)
    tree = build_parse_tree(expression)

    print "\nPreorder traversal:"
    preorder_traversal(tree)

    print "\nInorder traversal:"
    inorder_traversal(tree)

    print "\nPostorder traversal:"
    postorder_traversal(tree)

    print "\nPostorder evaluation:"
    print "Value: {}".format(postorder_evaluation(tree))

    print "\nReconstructing expression from tree:"
    print print_expression(tree)
