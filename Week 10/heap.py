class Entry:
    def __init__(self,item,priority):
        self.item = item
        self.priority = priority

    def __lt__(self,other):
        return self.priority < other.priority

class Heap:
    def __init__(self):
        self._L = []

    def put(self,item,priority):
        self._L.append(Entry(item,priority))
        self.upheap()

    def upheap(self):
        i = len(self._L)-1
        p = self.parent(i)

        while p and self._L[p]> self._L[i]:
            self._L[p], self._L[i] = self._L[i],self._L[p]
            i = p
            p = self.parent(i)

    def parent(self, i):
        if i == 0: return None
        return (i -1) // 2
    