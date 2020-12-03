from collections import deque
class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        # root, left, right
        values = []
        def walk(position):
            if not position:
                return
            values.append(position.value)
            walk(position.left)
            walk(position.right)
        walk(self.root)
        return values

    def in_order(self):
        # left, root, right
        values = []
        def walk(position):
            if not position:
                return
            walk(position.left)
            values.append(position.value)
            walk(position.right)
        walk(self.root)
        return values

    def post_order(self):
        # left, right, root
        values = []
        def walk(position):
            if not position:
                return
            walk(position.left)
            walk(position.right)
            values.append(position.value)
        walk(self.root)
        return values

    def add(self, value):
        new_n = Node(value)
        queue = Queues()
        if self.root != None:
            queue.enqueue(self.root)

            while not queue.is_empty():
                top = queue.dequeue()
                if not top.left:
                    top.left = new_n
                    return
                if top.right == None:
                    top.right = new_n
                    return
                if top.left:
                    queue.enqueue(top.left)
                if top.right:
                    queue.enqueue(top.right)
        else:
            self.root = new_n
        return


    def breadth_first(self): # goes from top to bottom and left to right for each tree row
        queue = Queues()
        collection = []
        queue.enqueue(self.root) # start at top

        while not queue.is_empty():
            top = queue.dequeue()
            collection.append(top.value)
            if collection.left != None:
                queue.enqueue(top.left)
            if collection.right != None:
                queue.enqueue(top.right)
        return collection


class Queues:
    def __init__(self):
        self.container = deque()

    def is_empty(self):
        len(self.container) == 0
        return

    def enqueue(self, value):
        self.container.appendleft(value)

    def dequeue(self):
        self.container.pop()
        return

    def peek(self):
        if self.container:
            return self.container[-1]


class BinarySearchTree(BinaryTree):
    def add(self, value):
        new_n = Node(value)

        def configure(position, new):
            if not position:
                return
            if new_n.value < position.value:
                if not position.left:
                    position.left = new_n
                else:
                    configure(position.left, new_n)
            else:
                if not position.right:
                    position.right = new_n
                else:
                    configure(position.right, new_n)
        if not self.root:
            self.root = new_n
            return self.root
        configure(self.root, new_n)

    def contains(self, value):
        if values not in self.pre_order():
            return False
        else:
            return True




tree_stuff = BinarySearchTree()
tree_stuff.add(2)
tree_stuff.add(7)
tree_stuff.add(5)
tree_stuff.add(10)
tree_stuff.add(0)
tree_stuff.pre_order()

