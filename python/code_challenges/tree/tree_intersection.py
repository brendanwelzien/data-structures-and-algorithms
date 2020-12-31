from tree import Node, BinarySearchTree, BinaryTree
from stacks_and_queues.stacks_and_queues import Queue

def tree_intersection(treeOne, treeTwo):
    identical = []
    tree_one = TreeOne.pre_order()
    tree_two = TreeTwo.pre_order()

    for potential_identical in tree_one:
        if potential_identical in tree_two:
            identical.append(potential_identical)
    return identical
