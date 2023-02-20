class Node:
    def __init__(self, _data, _next = None):
        self._data = _data
        self._next = _next

    def __str__(self):
        if self._next is not None:
            return (f"Node(data = {self._data}, next._data = {self._next._data})")
        else:
            return (f"Node(data = {self._data}, next._data = None)")

class LinkedList:

    def __init__(self):
        self._head = None
        self.len = 0

    def add_first(self, _data):
        new_node = Node(_data, self._head)
        new_node._next = self._head
        self._head = new_node
        self.len += 1

    def __len__(self):
        return self.len

    def remove_first(self):

        if len(self) == 0: raise IndexError("Cannot remove from empty linked list")

        data = self._head._data
        self._head = self._head._next
        self.len -= 1
        return

    def printLL(self):
        cur = self._head
        print("")
        while(cur):
            if cur._next is not None:
                print(cur._data, end=", ")
            else:
                print(cur._data)
            cur = cur._next
        print("")


ll = LinkedList()

ll.add_first("car")
ll.add_first("cat")
ll.add_first("pie")
ll.add_first("cargo")


ll.remove_first()

ll.add_first("protein")

ll.printLL()
ll.remove_first()
ll.remove_first()
ll.remove_first()

ll.printLL()
ll.remove_first()
