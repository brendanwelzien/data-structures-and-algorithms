class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self,value):
        self.head = Node(value, self.head)

    def append(self, value):
        current = self.head
        while current != None:
            if current.next == None:
                current.next = value
                break
            else:
                current = current.next

    def insert_before(self, value, newVal):
        if value == self.head:
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

    def kth_from_end(self, k):
        list = []
        current = self.head
        if k < 0:
            raise valueError("value of k should be positive")
        count = 0
        while current != None:
            if count == k:
                value_seeking = self.head
            elif count > k:
                value_seeking = value_seeking.next
            current = current.next
            count+= 1
        if count > k:
            return value_seeking.value

def zip_lists(lista, listb):
    list_a_node = lista.head
    list_b_node = listb.head
    zip_list = Linked_list()

    while list_a_node or list_b_node:
        if list_a_node:
            zip_list.append(list_a_node.value)
            list_a_node = list_a_node.next
        if list_b_node:
            zip_list.append(list_b_node.value)
            list_b_node = list_b_node.next
    return zip_list

    def __str__(self):
        l_str = str()
        c_node = self.head
        if not c_node:
            return 'None'
        while c_node.next:
            c_node = c_node.next
            l_str += str(c_node.value) + ' -> '
        l_str += str(c_node.value) + ' -> None'
        return l_str
