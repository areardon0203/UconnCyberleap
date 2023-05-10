import unittest 
from hw10 import Entry, MaxHeap


class TestEntry(unittest.TestCase):
    def test_one_level_priority(self):
        e1 = Entry(priority=[0], item ="Jake")
        e2 = Entry(priority=[1], item="Rachel")
        self.assertGreater(e2, e1)
        print("Passed 1 level!")
    def test_two_level_priority(self):
        e1 = Entry(priority=[1,"a"], item ="Jake")
        e2 = Entry(priority=[1,"b"], item="Rachel")
        e3= Entry(priority=[0,"C"], item="Tobias")
        self.assertGreater(e2, e1)
        print("Passed 2 level!")

    def test_three_level_priority(self):
        e1 = Entry(priority=[1,"a",3.72], item ="Jake")
        e2 = Entry(priority=[1,"b",4.73], item="Rachel")
        self.assertGreater(e2, e1)
        print("Passed 3 level!")

    def test_Equal(self):
        e1 = Entry(priority=[1,"a",3.72], item ="Jake")
        e2 = Entry(priority=[1,"a",3.72], item="Rachel")
        self.assertEqual(e2, e1)
        print("Passed Equal!")

    def test_Unequal(self):
        e1 = Entry(priority=[1,"a",3.72], item ="Jake")
        e2 = Entry(priority=[1,"b",3.72], item="Rachel")
        self.assertNotEqual(e2, e1)
        print("Passed Unequal!")

    def test_unequal_priority_list_length(self):
        e1 = Entry(priority=[0],item="")
        e2 = Entry(priority=[0,"b"],item="")
        self.assertGreater(e2, e1)
        self.assertLess(e1,e2)
        print("Passed smallest priority")

    def test_unequal_priority_list_length_opp(self):
        e1 = Entry(priority=[0,"a"],item="")
        e2 = Entry(priority=[0],item="")
        self.assertGreater(e1,e2)
        self.assertLess(e2,e1)
        print("Passed smallest priority")


class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        self.heap = MaxHeap()
        print("heap initialized")
    
    def print_heap(self):
        for entry in self._entries:
            print(f"Item: {entry.item}, Priority: {entry.priority}")

    def test_insert_and_findmax(self):
        insertions = [('A', 5), ('B', 10), ('C', 3), ('D', 8)]
        for item, priority in insertions:
            self.heap.insert(item, priority)
        self.assertEqual(self.heap.findmax(), 'B')
        print("Find Max Successful")

    def test_removemax(self):
        insertions = [('A', 5), ('B', 10), ('C', 3), ('D', 8)]
        for item, priority in insertions:
            self.heap.insert(item, priority)
        max_item = self.heap.removemax()
        self.assertEqual(max_item, 'B')
        self.assertEqual(self.heap.findmax(), 'D')
        max_item = self.heap.removemax()
        self.assertEqual(self.heap.findmax(), 'A')
        print("Remove Max Successful")

    def test_len(self):
        insertions = [('A', 5), ('B', 10), ('C', 3), ('D', 8)]
        for item, priority in insertions:
            self.heap.insert(item, priority)
        self.assertEqual(len(self.heap), 4)
        self.heap.removemax()
        self.assertEqual(len(self.heap), 3)
        self.heap.removemax()
        self.assertEqual(len(self.heap), 2)
        print("Length Test Successful")

    def test_empty_heap(self):
        with self.assertRaises(RuntimeError):
            self.heap.findmax()
        with self.assertRaises(RuntimeError):
            self.heap.removemax()
        print("Empty Heap Errors Succesful")

   
unittest.main()