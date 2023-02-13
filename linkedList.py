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

    def remove_last(self):
        #Edge case: LL is empty
        if len(self) == 0:
            raise IndexError("Cannot remove from empty linked list")
        #Edge case: LL has only 1 item
        if len(self) == 1:
            #[head] --> None._next
            item = self._head._item #retrieve item
            self._head = None       #cut off tail( tail is head)
            self._len -= 1          #update length
            return item             #return item

        #"Typical" case: LL has 2+ items
        #find penultimate of linked list
        penult = self._head
        while penult._next._next is not None:
            penult = penult._next

        item = penult._next._item       #retrieve data
        penult._next = None             # cut off tail
        self._len -= 1                  #update length
        return item                     #return item

    def add_last(self, item):
        
        #edge case: empty LL

        if len(self) == 0: return self.add_first(item)

        #"Typical" case: 1+ nodes in LL
        tail = self._head
        while tail._next is not None:
            tail = tail._next
        
        tail._next = Node(item, None)
        self._len += 1

    def remove_first(self):
    #edge case: empty LL
        if len(self)== 0: raise IndexError("Cannot remove from empty linked list")

    #"typical" case: 1+ nodes

        item = self._head._item         #extract data
        self._head = self._head._next   #cut off head
        self._len -= 1                  #update length
        return item


if __name__=='__main__':
    
    ll = LinkedList()
    n = 10

    for i in range(n): ll.add_first(i)
    for i in range(n): assert ll.remove_last() == i
    print("add_first and remove_last work")

    ll = LinkedList()
    for i in range(n): ll.add_last(i)
    for i in range(n): assert ll.remove_first() == i
    print("add_last and remove_first works!!")


    # for i in range(n): 
    #     print(f"ll.head = {ll._head}")
    #     ll.add_first(i)
    # print()
    # for i in range(n):
    #     print(f"ll._head={ll._head}")
    #     assert ll.remove_last() == i

    # print(f"ll._head = {ll._head}")