from ds2 import *

class AnotherStack(ListStack):
    def pop(self):
        try:
            return self._L.pop()
        except IndexError:
            raise RuntimeError("pop from empty stack...there ain't nothing there!")

s = AnotherStack()
s.push(5)
s.pop()




class ListQueue(ListQueueFakeDelete):
    def dequeue(self):
        item = self._L[self._head]
        self._head += 1
        if self._head > len(self._L)//2:
            self._L = self._L[self._head:]
            self._head = 0
        return item