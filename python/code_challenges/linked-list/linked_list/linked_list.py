class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def append(self, value):
        current = self.head
        while current != None:
            if current.next == None:
                current.next = value
                break
            else:
                current = current.next

    def insert_before(self, value, newVal):
        if value = self.head:
            self.head == newVal
            newVal.next = value
        else:
            current = self.head
            while current.next != value:
                if current.next.next == value:
                    current.next = newVal
                    newVal.next = value
                    break
                else:
                    current.next = current.next.next


