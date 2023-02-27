class Task:
    """Initialized a node with the behaviors necessary for a task."""
    def __init__(self, _id, _cycles_left, _next = None, _prev = None):
        self._id = _id
        self._cycles_left = _cycles_left
        self._next = _next 
        self._prev = _prev
        self._reduce_cycles = 1

class TaskQueue:
    """A class for managaing tasks"""
    def __init__(self):
        """Initiliazes a new Task queue"""
        self._tail = None
        self._len = 0

    def add_task(self, _id, _cycles):
        """add a new node to the beginning of the linked list"""
        if self._len == 0: 
            """checks if adding a first node to queue"""
            new_node = Task(_id, _cycles)
            self._tail = new_node

        elif self._len == 1:
            """checks if there is already a single node, maps 2 nodes through next and previous pointers"""
            new_node = Task(_id, _cycles, self._head, self._head)
            self._head._prev = new_node
            self._head._next = new_node
            
        else:
            """If more than one node, maps nodes proper sequence"""
            new_node = Task(_id, _cycles, self._head, self._tail)
            # self._tail._next = new_node
            self._head._prev = new_node       
            self._head._next = new_node._next._next
            self._tail._next = new_node

            # self._tail._next = new_node
            # new_node._prev = self._tail
        """initializes new node as the head node regardless of how many nodes currently exist and adds 1 the queue length"""
        self._head = new_node
        self._len += 1

    def __len__(self):
        """returns the length of task queue."""
        return self._len

    def remove_task(self, _id):

        """Pulls the id of the current head within the cycle of execute tasks """
        id = _id

        # Edge case if list is empty
        if self._len == 0: raise IndexError("Cannot remove from empty linked list")

        if self._len == 1:
            """Sets head and tail to none and subtracts 1 from length of list."""
            self._head = None
            self._tail = None
            self._len -= 1
            return id

        # if self._len == 2:
        #     self._head = id
        #     self._tail = self._head._prev
        #     self._head._prev._next = self._head._next
        #     self._head = self._head._next
        #     self._len -= 1
        #     return id

        else:
            """Sets the next and previous pointers to overide current nodes next and previous pointers."""
            self._head = id
            self._head._next._prev = self._head._prev
            self._head._prev._next = self._head._next
            self._head = self._head._next
            self._len -= 1
            return id
        
    
    def is_empty(self):
        """Checks to find out if list is empty."""
        if self._len == 0: raise RuntimeError("this task queue is empty")
        else: return False

    def execute_tasks(self):
        """Sets a loop to cycle through all tasks"""
        cur = self._head
        while cur:
            if self._len == 0:
                """Checks if task queue is empty and returns a string"""
                return str("There is nothing left in the queue")
            if cur._cycles_left > 0:
                """checks to see if any tasks are left and prints out the task id and how many cycles it has remaining"""
                cur._cycles_left -= cur._reduce_cycles
                print(f"{cur._id} has {cur._cycles_left} cycles remaining")
                cur = cur._next
            else:
                """Launches funciton for task to be removed when it has no more cycles left. Sets current node to next node to continue executing remaining tasks."""
                TaskQueue.remove_task(self, cur)
                cur = cur._next

 