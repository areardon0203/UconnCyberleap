from taskQueue import *
import unittest 


tq = TaskQueue()
# tq.add_task(1,15)
# tq.add_task(2,20)
# tq.add_task(3,10)
# tq.add_task(4,3)
# tq.add_task(5,10)
# tq.add_task(6,2)
# tq.execute_tasks()
# print("done")



class MyTestCaseTask(unittest.TestCase):
    """Tests to make sure that nodes are properly initialized."""
    def test_init(self):
        task = Task(5,20,30)   
        assert task._id == 5
        assert task._cycles_left == 20
        assert task._reduce_cycles == 1
        print("Task was created properly")

class MyTestCaseTaskqueue(unittest.TestCase):
    
    """Tests to make sure that when tasks are added to the que, nodes are properly mapped to each other."""
    def test_add_task(self):
        tq.add_task(1,15)
        tq.add_task(2,20)
        tq.add_task(3,10)
        assert tq._len == 3
        assert tq._head._id == 3
        assert tq._head._next._id == 2
        assert tq._head._prev._id == 1
        print("passed add_task")


    def test_execute_tasks(self):
        """"Tests to make sure that items all items are executed until nothin remains in the que."""
        assert tq.execute_tasks() == str("There is nothing left in the queue")
        print('Properly executed all tasks')


    # def test_is_empty(self):
    #     with self.assertRaises(RuntimeError): 
    #         tq.is_empty()
    #         print("Runtime Error Passed")


if __name__ == '__main__':
    unittest.main()



# for task in range(n): dll.add_first(task)
# for task in range(n): assert dll.remove_last() == task

# print("add first/last works!")