
class LinkedList:

    def __init__(self): # head property that is empty
        self.head = None


    def insert(self, value): # adds a node to the head
        self.head = Node(value, self.head)

    def includes(self, value): # return boolean if value exists
        currentPlace = self.head
        while currentplace:
            if currentplace.value == value:
                return True
            currentplace = currentplace.next_n
        return False

    def to_string(self):
        currentplace = self.head
        string_of_values = ""
        while currentplace:
            string_of_values+= f" { {str(currentplace.value)} } ->"
            currentplace = currentplace.next_n # move on to next node
        return string_of_values.replace("'"," ") + " NULL" # final string

    def __repr__(self):
        return self.to_string()

class Node:
    def __init__(self, value, next_n=None): # next = pointer to next node
        self.value=value
        self.next_n=next_n
