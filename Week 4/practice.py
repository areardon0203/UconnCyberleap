

class Stack:
    def __init__(self):
        self._L = []

    def push(self, item):
        self._L.append(item)
        

    def pop(self):
        return self._L.pop()

    def __len__(self):
        return len(self._L)

    def peek(self):
        return self._L[-1]

    def is_empty(self):
        return len(self._L) == 0


if __name__ == "__main__":

    s = Stack()

    n = 10

    for i in range(n):
        s.push(i)

    for i in range(n):
        assert s.pop() == n - 1 - i

    assert s.is_empty()

    for i in range(n):
        assert len(s) == i
        s.push(i)
        assert not s.is_empty()

    assert len(s) == n
    
    print("all done!")