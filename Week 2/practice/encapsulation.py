class MyLimitedList:
    def __init__(self):
        self._L = []
    def append(self, item):
        self._L.append(item)
    def __getitem__(self, index):
        return self._L[index]   

L = MyLimitedList()
L.append(1)
L.append(15)
L.append(20)
L.append(7)

print(L[3])