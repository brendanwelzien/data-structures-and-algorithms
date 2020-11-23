class Node:
    def __init__(self, value, next_p=None):
        self.next = next_p
        self.value = value

    def __str__(self):
        return f'{self.value}'

class InvalidOperationError(Exception):
    pass


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        current = self.top
        if self.top == None:
            self.top = Node(value)
        else:
            node_n = Node(value)
            node_n.next = self.top
            self.top = node_n

    def pop(self):
        if not self.top:
            raise InvalidOperationError('Method not allowed on empty collection')

        if self.top:
            top_value = self.top
            self.top = self.top.next
            return top_value.value

    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        return not self.top

class Queue:
    def __init__(self):
        self.f = None
        self.r = None

    def enqueue(self, value):
        node = Node(value)

        if self.r:
            node = self.r.next
            node = self.r

    def dequeue(self):
        if not self.f:
            raise InvalidOperationError('Method not allowed on empty collection')

        leave = self.f
        if self.f == self.r:
            self.r = None
        self.f = self.f.next
        return leave.value

    def peek(self):
        if not self.f:
            raise InvalidOperationError('Method not allowed on empty collection')
        return self.f.value

    def is_empty(self):
        return not self.f and not self.r
