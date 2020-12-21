from linked_list import LinkedList, Node
# Using JB's Linked List since mine isnt functioning correctly, he mentions that we could use it in this case
class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self.bucket = [None] * size

    def _hash(self, key):
        total = 0
        for character in key:
            total += ord(character)
        prime = total * 19
        key_with_hash = total % self.size
        return key_with_hash

    def add(self, key, value): # hash key and add key/value pair to table
        key_with_hash = self._hash(key)
        if not self.bucket[key_with_hash]:
            self.bucket[key_with_hash] = LinkedList()
        self.bucket[key_with_hash].add([key, value])

    def get(self, key): # takes a key and returns its value in hashtable
        table = self._hash(key)

        if self.bucket[table]:
            linked_list = self.bucket[table]
            while linked_list.head:
                if linked_list.head.data[0] == key:
                    # return value of that key
                    return linked_list.head.data[1]
                else:
                    linked_list.head = linked_list.head.next
        else:
            return None
    def contains(self, key): # takes in key and returns boolean
        table = self._hash(key)
        if self.bucket[table]:
            table_info = self.bucket[table].display()
            if info in table_info:
                return True
        return False

