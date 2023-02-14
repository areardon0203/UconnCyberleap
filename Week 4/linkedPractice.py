class Node:
    def __init__(self, _data, _next = None):
        self._data = _data 
        self._next = _next 

    def __str__(self):
        if self._next is not None:
            return (f"self.data = {self._data}, self._next = {self._next._data}")
        return (f"self.data = {self._data}, self._next = none")

class LinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def add_to_front(self, _data):
        new_node = Node(_data, self._head)    
        self._head = new_node
        self._len += 1

    def len(self):
        return self._len
        
            


ll = LinkedList()
