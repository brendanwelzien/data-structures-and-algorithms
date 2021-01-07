class Node:
    def __init__(self, value, _next=None):
        self.value = val
        self.next = _next

    def __repr__(self):
        return f"{self.next}'s value is {self.value}"

class linkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        self.head = Node(value, self.head)

    def includes(self, value):
        # check if value exists in Node
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append_to_tail(self, value):
        current = self.head
        while current:
            if not current.next:
                current.next = Node(value)
            current = current.next
# More linked list tomorrow
