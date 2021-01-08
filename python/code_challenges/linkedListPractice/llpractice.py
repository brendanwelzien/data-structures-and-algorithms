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

    def insert_value_before(self, value, newValue):
        current = self.head
        while current:
            if not current.next:
                return 'empty value in list'
            if current.next.value == value:
                current.next = Node(newValue, current.next)
            current = current.next

    def insert_value_after(self, value, newValue):
        current = self.head
        while current:
            if not current.next:
                return 'empty value in list'
            if current.value == value:
                current.next = Node(newValue, current.next)
            current = current.next

    def check_kth(self, k):
        current = self.head
        new_list = []
        if k < 0:
            raise ValueError("improper value")
        if len(new_list) < k:
            raise IndexError("value improper length in list")
        while current:
            new_list.append(current)
            current = current.next
        new_list.reverse()
        if k == len(new_list):
            k -= 1
            return new_list[k].value 

