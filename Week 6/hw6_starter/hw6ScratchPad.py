# class OrderedListSimple:
#     def __init__(self):
#         self._L = []
    
#     def add(self,item):
#         self._L.append(item)
#         self._L.sort()

#     def remove(self, item):
#         self._L.remove(item)

#     def __getitem__(self,index):
#         return self._L[index]
    
#     def __contains__(self,item):
#         left, right = 0, len(self._L)
#         while right - left > 1:
#             median = (right + left) // 2
#             if item < self._L[median]:
#                 right = median
#             else:
#                 left = median
#         return right > left and self._L[left] == item
    
#     def __len__(self):
#         return len(self._L)
    
#     def __iter__(self):
#         return iter(self._L)
    

# mylist = OrderedListSimple()

# mylist.add(5)
# mylist.add(3)
# mylist.add(7)
# mylist.add(1)
# print(4 in mylist)


def sortedornot(L):
    for i in range(len(L)-1):
        if L[i]> L[i+1]:
            return False
    return True

def dumbersort(L):
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]
    return L

def bubblesort(L):
    for iteration in range(len(L)-1):
        for i in range(len(L)-1):
            if L[i]>L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]

alist = [30, 100000,54,26,93,17,77,31,44,55,20]
bubblesort(alist)
print(alist)

numbers = [5, 2, 9, 1, 5, 6]
dumbersort(numbers)
print(numbers)

# print(sortedornot([1,2,3,4,5,6]))

# print(sortedornot([1,4,3,2,5,6]))