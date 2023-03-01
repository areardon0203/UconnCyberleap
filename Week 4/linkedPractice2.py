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
        return data

    def remove_last(self):

        """edge case empty list"""
        if len(self) == 0: raise IndexError("Cannot remove from an empty list")

        """edge case only 1 item"""
        if len(self) == 1:
            data = self._head._data
            self._head = None
            self.len -= 1
            return data

        """"typical case"""
        penult = self._head
        while penult._next._next is not None:
            penult = penult._next
        data = penult._next._data
        penult._next = None
        self.len -= 1 
        return data

    def add_last(self, data):

        if len(self) == 0: return self.add_first(data)

        tail = self._head
        while tail._next is not None:
            tail = tail._next
        tail._next = Node(data)
        self.len += 1

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


if __name__ == '__main__':

    ll = LinkedList()

    n = 10

    for i in range(n): ll.add_first(i)
    for i in range(n): assert ll.remove_last() == i
    print("works!")

    for i in range(n): ll.add_last(i)
    for i in range(n): assert ll.remove_first() == i
    print("second statement works")