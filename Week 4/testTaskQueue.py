from taskQueue import *


dll = DoublyLinkedList()
n = 10

for task in range(n): dll.add_first_task(task)
for task in range(n): assert dll.remove_last_task() == task

print("add first/last works!")