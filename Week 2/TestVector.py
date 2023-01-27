import unittest
import math
from Vector import RecVec #PolVec

class TestRecVec(unittest.TestCase):
    """Test the class RecVec in the file Vector.py"""   
    def test_init(self):
        """Tests that the initialization of object creation is receiving proper values."""
        rv = RecVec(3,4)
        self.assertEqual(rv.x, 3)
        self.assertEqual(rv.y, 4)
        print("RecVec Init Test Passed!")
    
    def test_add(self):
        """Tests that the add function is returning an appropriate tuple"""
        v1 = (3,4)
        v2 = (7,8)
        added = RecVec.__add__(self,v1,v2)
        self.assertEqual(added, (10,12))
        print("Passed add")

    def test_sub(self):
        """Tests that the add function is returning an appropriate tuple"""
        v1 = (7,8)
        v2 = (3,4)
        subtracted = (RecVec.__sub__(self,v1,v2))
        self.assertEqual(subtracted, (4,4))
        print("Passed Subtraction")

    def test_eq(self):
        """Tests that two tuples are eqivelant"""
        v1 = RecVec(3,4)
        v2 = RecVec(3,4)
        self.assertEqual(v1.x,v2.x)
        self.assertEqual(v1.y,v2.y)
        print("Passed Equal")
        
    def test_str(self):
        """Tests that we are returning a readable string."""
        rv = RecVec(3,4)
        self.assertEqual(str(rv), f"RecVec(x = {rv.x} y = {rv.y})")
        print("Passed String Test")
        
    def test_pol(self):
        rv = RecVec(3,4)
        recPol = rv.pol()
        self.assertEqual(recPol,(5, 53))
        print("Passed Polar Coordinate test")

    def test_rec(self):
        """Tests to make sure that the rectangular coordinates are returned in a tuple"""
        rec = RecVec(3,4)
        recCor = RecVec.rectangular(rec)
        self.assertEqual(recCor, (3,4))
        print("Passed Rec test")

    def test_get_x(self):
        """Tests that the value of x is returned properly as a single value"""
        rv = RecVec(3,4)
        self.assertEqual(rv.get_x(),3)
        print("Passed get_x")
    
    def test_get_y(self):
        """Tests that the value of y is returned properly as a single value"""
        rv = RecVec(3,4)
        self.assertEqual(rv.get_y(),4)
        print("Passed get_y")

    def test_get_mag(self):
        """Tests to make sure that the objects magnitude is properly returned"""
        rv = RecVec(3,4)
        self.assertEqual(rv.mag(),(5))
        print("Passed get_mag")

#   def test_get_ang(self):


# class TestPolVec(unittest.TestCase):
#     def test_init(self):
#         pv = PolVec(6,10)
#         self.assertEqual(pv.mag, 6)
#         self.assertEqual(pv.ang, 10)
#         print("PolVec INIT Test Passed!")

unittest.main()