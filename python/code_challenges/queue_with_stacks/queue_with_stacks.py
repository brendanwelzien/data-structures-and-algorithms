class PseudoQueue:
    def __init__(self):
        self.main = Stack()
        self.temp = Stack()

    def dequeue(self):
        while not self.main.is_empty():
            self.temp.push(self.main.pop())

        if self.temp.is_empty():
            raise IndexError('dequeuing not possible')

        temporary = self.temp.pop()
        return temporary

    def enqueue(self, value):
        self.main.push(value)

class Node:
    def __init__(self, value, next_n=None):
        self.value = value
        self.next = next_n

    def __str__(self):
        return f'{self.value} : {self.next}'

class Stack:
    def __init__(self):
        self.top = None

    def __str__(self):
        current = self.top
        outgoing = ''
        while current != None:
            outgoing += f'{current.value}'
            current = current.next
        return outgoing + 'NULL'

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

