class Deque:
    def __init__(self):
        self._L = []

#O(n)
    def add_first(self, item):
        self._L.insert(0,item)

    def add_last(self, item):
        self._L.append(item)
    
    def remove_first(self):
        return self._L.pop(0)

    def remove_last(self):
        return self._L.pop()

if __name__ == '__main__':
    d = Deque()
    n = 10

    for i in range(n): d.add_first(i)
    for i in range(n): assert d.remove_last() == i

    print("add first/remove last worked!")

    d = Deque()
    for i in range(n): d.add_last(i)
    for i in range(n): assert d.remove_first()==i
    
    print("add last/remove first worked!")
