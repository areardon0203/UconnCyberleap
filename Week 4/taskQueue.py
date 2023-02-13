

'''create a node object'''
class Node:
    def __init__(self, _task):
        self._task = _task #whatever task
        self._next = None #node or None 
        self._prev = None #node or None

    def __str__(self):
        if self._next is not None:
            return (f"Node(task = {self._task}, next._task = {self._next._task})")
        return(f"Node(task = {self._task},  (next = None)")

class DoublyLinkedList():
    def __init__(self):
        self._head = None
        self._len = 0

    def add_first_task(self, task):
        new_task = Node(task,_nex = self._head)   # create new node
        self._head = new_task               # update LL head
        self._len += 1

    def __len__(self):
        return self._len

    def remove_last_task(self):
        #Edge case: LL is empty
        if len(self) == 0:
            raise IndexError("Cannot remove from empty linked list")
        #Edge case: LL has only 1 task
        if len(self) == 1:
            #[head] --> None._next
            task = self._head._task #retrieve task
            self._head = None       #cut off tail( tail is head)
            self._len -= 1          #update length
            return task             #return task

        #"Typical" case: LL has 2+ tasks
        #find penultimate of linked list
        penult = self._head
        while penult._next._next is not None:
            penult = penult._next

        task = penult._next._task       #retrieve data
        penult._next = None             # cut off tail
        self._len -= 1                  #update length
        return task                     #return task