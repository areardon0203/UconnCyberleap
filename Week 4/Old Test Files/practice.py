class Node:
    def __init__(self, _item, _next):
        self._item = _item #whatever item
        self._next = _next #node or None

    def __str__(self):
        if self._next is not None:
            return (f"Node(item = {self._item}, next._item = {self._next._item})")
        return(f"Node(item = {self._item},  (next = None)")

class LinkedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def add_first(self, item):
        new_node = Node(item, self._head)   # create new node
        self._head = new_node               #update LL head
        self._len += 1

    def __len__(self):
        return self._len


ll= LinkedList()
