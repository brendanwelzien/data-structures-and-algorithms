
from tree import BinaryTree, Node, BinarySearchTree
from stacks_and_queues.stacks_and_queues import Queue
from tree_intersection import tree_intersection

def test_pre_order():
    tree_stuff = BinarySearchTree()
    tree_stuff.add(5)
    tree_stuff.add(6)
    tree_stuff.add(7)
    tree_stuff.add(8)
    actual = tree_stuff.pre_order()
    expected = [5, 6, 7, 8]
    assert actual == expected

def test_tree_intersection():
    tree_stuff = BinarySearchTree()
    tree_stuff_two = BinarySearchTree()

    tree_stuff.add(8)
    tree_stuff.add(9)
    tree_stuff.add(10)
    tree_stuff_two.add(9)
    tree_stuff_two.add(10)
    tree_stuff_two.add(11)
    actual = tree_intersection(tree_stuff, tree_stuff_two)
    expected = [9, 10]
    assert actual == expected

def test_tree_intersection_two():
    tree_stuff = BinarySearchTree()
    tree_stuff_two = BinarySearchTree()

    tree_stuff.add(7)
    tree_stuff.add(8)
    tree_stuff.add(9)
    tree_stuff.add(10)

    tree_stuff_two.add(8)
    tree_stuff_two.add(9)
    tree_stuff_two.add(10)
    actual = tree_intersection(tree_stuff, tree_stuff_two)
    expected = [8, 9, 10]
    assert actual == expected
