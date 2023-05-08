class Entry:
    def __init__(self, item, priority):
        self.priority = priority
        self.item = item

    def __lt__(self,other):
        for i, p in enumerate(self.priority):
            if i >= len(other.priority):
                return False
            if p < other.priority[i]:
                return True
            elif p > other.priority[i]:
                return False
            
        return self.item < other.item
    
    def __gt__(self, other):
        for i, p in enumerate(self.priority):
            if i >= len(other.priority):
                # If other's priority is shorter, treat it as a maximum value
                return True
            if p > other.priority[i]:
                return True
            elif p < other.priority[i]:
                return False
        # If all priorities are equal, compare items
        return self.item > other.item
    
    def __eq__(self, other):
        return self.priority == other.priority and self.item == other.item
    
    def __ne__(self, other):
        return not self.__eq__(other)

class MaxHeap:
    def __init__(self):
        self._entries = []

    def insert(self,item,priority):
        self._entries.append(Entry(item,priority))

    def _parent(self,i):
        return (i - 1) // 2
    
    def _children(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._entries), right + 1))
        
    def _swap(self, a, b):
        L = self._entries
        L[a],L[b] = L[b], L[a]

    def _upheap(self, i):
        L = self._entries
        parent = self._parent(i)
        if i > 0 and L[i] > L[parent]:
            self._swap(i, parent)
            self._upheap(parent)
            
    def findmax(self):
        return self._entries[0].item

    def removemax(self):
        if len(self._entries) == 0:
            raise RuntimeError("Cannot remove from an empty heap")
        L = self._entries
        item = L[0].item
        L[0] = L[-1]
        L.pop()
        self._downheap(0)
        return item

    def _downheap(self, i):
        L = self._entries
        children = self._children(i)
        if children:
            child = max(children, key = lambda x: L[x])
            if L[child] > L[i]:
                self._swap(i,child)
                self._downheap(child)

    def __len__(self):
        return len(self._entries)



if __name__ == '__main__':
    S = SortedListPQ()
    S.insert("ham", 3)
    S.insert("cheese", 1)
    S.insert("bread", 2)
    S.insert("pasta", 4)
    S.insert("calzone", 1)
    print([S.removemin() for i in [1,2,3,4]])
