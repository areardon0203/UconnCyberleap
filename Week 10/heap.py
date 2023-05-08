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
    



    # class Heap:
    # def __init__(self):
    #     self._entries = []

    # def insert(self,item,priority):
    #     self._entries.append(Entry(item,priority))

    # def _parent(self,i):
    #     return (i - 1) // 2
    
    # def _children(self, i):
    #     left = 2 * i + 1
    #     right = 2 * i + 2
    #     return range(left, min(len(self_entries),right + 1))
        
    # def _swap(self, a, b):
    #     L = self._entries
    #     L[a],L[b] = L[b], L[a]

    # def _upheap(self, i):
    #     L = self._entries
    #     parent = self._parent(i)
    #     if i > 0 and L[i] < L[parent]:
    #         self._swap(i, parent)
    #         self._upheap(parent)
    # def findmin(self):
    #     return self._entries[0].item

    # def removemin(self):
    #     L = self._entries
    #     item = L[0].item
    #     L[0] = L[-1]
    #     L.pop()
    #     self._downheap(0)
    #     return item

    # def _downheap(self, i):
    #     L = self._entries
    #     children = self._children(i)
    #     if children:
    #         child = min(children, key = lambda x: L[x])
    #         if L[child] < L[i]:
    #             self._swap(i,child)
    #             self._downheap(child)

    # def __len__(self):
    #     return len(self._entries)
    