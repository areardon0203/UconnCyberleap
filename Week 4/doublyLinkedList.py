class Node:
    def __init__(self, _data, _next = None, _prev = None):
        self._data = _data
        self._next = _next
        self._prev = _prev

    def __str__(self):
        if self._next is not None:
            return (f"Node(data = {self._data}, next._data = {self._next._data}, prev._data ={self._prev._data})")
        else:
            return (f"Node(data = {self._data}, next._data = None, prev._data ={self._prev._data})")

class DoublyLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self.len = 0

    def __len__(self):
        return self.len

    def add_first(self, _data):
        """add a new node to the beginning of the linked list"""
        if self.len == 0: 
            new_node = Node(_data, None, None)
            self._tail = new_node
        else:  
            new_node = Node(_data, self._head, None)
            self._head._prev = new_node
        self._head = new_node
        self.len += 1

    def add_last(self, _data):
        """Sets node as head if linked list is empty"""
        if self.len == 0: return self.add_first(_data)

        """Searches for the end of the linked list and then inserts new at the end."""

        self._tail._next = Node(_data , None, self._tail) #set next node to none and previous node to previous tail 
        self._tail = self._tail._next
        self.len += 1

    def remove_first(self):
        # Edge case LL is empty 
        if self.len == 0: raise IndexError("Cannot remove from empty linked list")

        data = self._head._data
        self._head._prev = None
        self._head = self._head._next 
        self.len -= 1
        return data

    def remove_last(self):
        # Edge case LL is empty 
        if self.len == 0: raise IndexError("Cannot remove from empty linked list")
       
        #Edge case: LL has only 1 item
        data = self._tail._data
        self._tail._next = None
        self._tail = self._tail._prev
        self.len -= 1
        return data


    def printDLL(self):
        cur = self._head
        print("")
        while(cur):
            if cur._next is not None:
                print(cur._data, end=", ")
                cur = cur._next
            else:
                print(cur._data)
                return
        print("")



dll = DoublyLinkedList()

n = 10

# dll.add_first(4)
# dll.add_first(5)
# dll.add_first(7)
# dll.remove_last()
# dll.remove_first()

for i in range(n): dll.add_first(i)
for i in range(n): dll.remove_last()

print("passed test 1")

for i in range(n): dll.add_last(i)
for i in range(n): assert dll.remove_first() == i

# dll.printDLL()
print("passed test 2")

# dll.add_first("car")
# dll.add_first("cat")
# dll.add_first("pie")
# dll.add_last("cargo")

# ll.remove_last()


# for i in range(n): dll.add_first(i)
# dll.remove_first()
# dll.remove_last()

# dll.remove_last()
# for i in range(n): ll.remove_first() == i
# print("passed")

# print(ll.get_tail())

# dll.printDLL()