import unittest 
from hw10 import Entry, Heap


class TestEntry(unittest.TestCase):
    def test_one_level_priority(self):
        e1 = Entry(priority=[0], item ="Jake")
        e2 = Entry(priority=[1], item="Rachel")
        assert(e2 > e1)
        print("Passed 1 level!")
    def test_two_level_priority(self):
        e1 = Entry(priority=[1,"a"], item ="Jake")
        e2 = Entry(priority=[1,"b"], item="Rachel")
        e3= Entry(priority=[0,"C"], item="Tobias")
        assert(e2 > e1)
        print("Passed 2 level!")

    def test_three_level_priority(self):
        e1 = Entry(priority=[1,"a",3.72], item ="Jake")
        e2 = Entry(priority=[1,"b",4.73], item="Rachel")
        assert(e2 > e1)
        print("Passed 3 level!")

    def test_unequal_priority_list_length(self):
        e1 = Entry(priority=[0],item="")
        e2 = Entry(priority=[0,"b"],item="")
        assert(e2 > e1)
        assert(e1 < e2)
        print("Passed smallest priority")


class TestMaxHeap(unittest.TestCase):
    pass



unittest.main()