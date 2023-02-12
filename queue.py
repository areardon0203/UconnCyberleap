class Queue:
    def __init__(self):
        self._L = []
    
    #0(?)
    
    def enqueue(self, item):

        self._L.append(item)
    

    #0(?)

    def dequeue(self):
        return self._L.pop(0)

if __name__ == '__main__':
    q = Queue()
    n = 10 

    for i in range(n): q.enqueue(i)
    for i in range(n): assert q.dequeue() == i