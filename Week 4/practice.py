

class Stack:
    def __init__(self):
        self._L = []

    def push(self, item):
        self._L.append(item)
        

    def pop(self):
        return self._L.pop()


if __name__ == "__main__":

    s = Stack()

    n = 10

    for i in range(n):
        s.push(i)

    for i in range(n):
        assert s.pop() == n - 1 - i

    print("all done!")