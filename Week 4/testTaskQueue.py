from taskQueue import *
import unittest 


tq = TaskQueue()
tq.add_task(8,25)
tq.add_task(5,10)
tq.add_task(7,20)
tq.execute_tasks()

task = Task(5,20,30)   



# class MyTestCaseTask(unittest.TestCase):
    
    
 
#     def test_init(self):
   
#         assert task._id == 5
#         assert task._cycles_left == 20
#         assert task._reduce_cycles == 1
#         print("Task was created properly")

# class MyTestCaseTaskqueue(unittest.TestCase):

#     def test_add_first(self):
#         assert tq._head._id == 7
#         assert tq._head._next._id == 5
#         print("Passed head")

#     def test_len(self):
#         assert len(tq) == 2
#         print("length test passed")

#     def test_remove_task(self):
#         pass
    
#     def test_execute_tasks(self):
#         pass

#     # def test_is_empty(self):
#     #     with self.assertRaises(RuntimeError): 
#     #         tq.is_empty()
#     #         print("Runtime Error Passed")


        



# if __name__ == '__main__':
#     unittest.main()



# # for task in range(n): dll.add_first(task)
# # for task in range(n): assert dll.remove_last() == task

# # print("add first/last works!")