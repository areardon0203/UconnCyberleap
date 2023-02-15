class Node:
    def __init__(self, _data, _next):
        self._data = _data
        self._next = None
class LinkedList:
    def __init__(self):
        self._head = None
    
    def add_first(self, _data):
        new_node = Node(_data,self._head)
        self.head = new_node

    def len(self):
        return self.len()


ll = LinkedList

ll.add_first(5)
ll.add_first(6)
ll.add_first(10)

print(ll.head)