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
        # tail = self._head
        # while tail._next is not None:
        #     tail = tail._next
        self._tail._next = Node(_data , None, self._tail) #set next node to none and previous node to previous tail 
        self._tail = self._tail._next
        self.len += 1

    def remove_first(self):
        # Edge case LL is empty 
        if self.len == 0: raise IndexError("Cannot remove from empty linked list")

        #Edge case: LL has only 1 item
        data = self._head._data
        self._head = self._head._next
        self._head._prev = None 
        self.len -= 1
        return data

    def remove_last(self):
        # Edge case LL is empty
        if self.len == 0: raise IndexError("Cannot remove from empty linked list")
        
        #Edge case: LL has only 1 item
        if self.len == 1:
            #[head] --> None._next
            data = self._head._data #retrieve item
            self._head = None       #cut off tail( tail is head)
            self.len -= 1          #update length
            return data             #return item

        #"Typical" case: LL has 2+ items
        #find penultimate of linked list
        penult = self._head
        while penult._next._next is not None:
            penult = penult._next

        data = penult._next._data       #retrieve data
        penult._next = None             # cut off tail
        self.len -= 1                  #update length
        return data                     #return item


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



dll = DoublyLinkedList()

n = 10

# for i in range(n): ll.add_first(i)
# for i in range(n): assert ll.remove_last() == i

# print("passed test 1")

# for i in range(n): ll.add_last(i)
# for i in range(n): ll.remove_first() == i

# print("passed test 2")

# ll.add_first("car")
# ll.add_first("cat")
# ll.add_first("pie")
# ll.add_last("cargo")

# ll.remove_last()


for i in range(n): ll.add_first(i)
# for i in range(n): ll.remove_first() == i
# print("passed")

# print(ll.get_tail())

ll.printLL()