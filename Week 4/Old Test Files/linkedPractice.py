class Node:
    def __init__(self, _data, _next = None):
        self._data = _data
        self._next = _next


class LinkedList:
    
    def __init__(self):
        self._head = None

    def add_first(self, _data):
        new_node = Node(_data)
        new_node._next = self._head
        self._head = new_node

    def printList(self): 
        current = self._head 
        print("")
        while (current): 
            print (current._data) 
            current = current._next
        print("")

ll = LinkedList()

ll.add_first("car")
ll.add_first("cat")
ll.add_first("cow")

ll.printList()