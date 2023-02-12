class Queue:
    def __init__(self):
        pass
    
    #0(?)
    
    def enqueue(self):
        pass
    

    #0(?)

    def dequeue(self):
        pass


if __name__ == '__main__':
    q = Queue()

    n = 10 

    for i in range(n):
        q.enqueue(i)

    for i in range(n):
        assert q.dequeue() == i 