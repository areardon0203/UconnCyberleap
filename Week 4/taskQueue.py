class Task:

    def __init__(self, _id, _cycles_left, _next = None, _prev = None):
        self._id = _id
        self._cycles_left = _cycles_left
        self._next = _next 
        self._prev = _prev
        self._reduce_cycles = 1

class TaskQueue:

    def __init__(self):
        self._tail = None
        self._len = 0

    def add_task(self, _id, _cycles):
        """add a new node to the beginning of the linked list"""
        if self._len == 0: 
            new_node = Task(_id, _cycles)
            self._tail = new_node
        else:  
            new_node = Task(_id, _cycles, self._head)
            new_node._next = self._head
            new_node._prev = self._tail
            self._tail._next = new_node
        self._head = new_node
        self._len += 1

    def __len__(self):
        return self._len

    def remove_task(self):
        # Edge case LL is empty 
        # if self.len == 0: raise IndexError("Cannot remove from empty linked list")
        id = self._id
        self._prev._next = self._next
        self._next._prev = self._prev
        self._prev = None
        self._head = self._next
        self._len -= 1
        return id

    def is_empty(self):
        if self._len == 0: raise RuntimeError("this task queue is empty")

    def execute_tasks(self):
        cur = self._head
        while cur:
            if cur._cycles_left > 0:
                cur._cycles_left -= cur._reduce_cycles
                print(f"{cur._id} has {cur._cycles_left} remaining")
                cur = cur._next
            else:
                TaskQueue.remove_task(cur)

    # def add_first(self, _data):
    #     """add a new node to the beginning of the linked list"""
    #     if self.len == 0: 
    #         new_node = Task(_data, None, None)
    #         self._tail = new_node
    #     else:  
    #         new_node = Task(_data, self._head, None)
    #         self._head._prev = new_node
    #     self._head = new_node
    #     self.len += 1

    # def add_last(self, _data):
    #     """Sets node as head if linked list is empty"""
    #     if self.len == 0: return self.add_first(_data)

    #     """Searches for the end of the linked list and then inserts new at the end."""

    #     self._tail._next = Task(_data , None, self._tail) #set next node to none and previous node to previous tail 
    #     self._tail = self._tail._next
    #     self.len += 1



    # def remove_last(self):
    #     # Edge case LL is empty 
    #     if self.len == 0: raise IndexError("Cannot remove from empty linked list")
       
    #     #Edge case: LL has only 1 item
    #     data = self._tail._data
    #     self._tail._next = None
    #     self._tail = self._tail._prev
    #     self.len -= 1
    #     return data

