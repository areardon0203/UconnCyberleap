import unittest
from Vector import RecVec, PolVec

class TestRecVec(unittest.TestCase):
    """Test the class RecVec in the file Vector.py"""
   
    def test_init(self):
        """Tests that the initialization of object creation is receiving proper values."""
        rv = RecVec(3,4)
        self.assertEqual(rv.x, 3)
        self.assertEqual(rv.y, 4)
        print("RecVec Test Passed!")
    
    def test_add(self):
        """Tests that the add function is returning an appropriate tuple"""
        v1 = (3,4)
        v2 = (7,8)
        added = RecVec.__add__(self,v1,v2)
        self.assertEqual(added, (10,12))
        print("Passed Adding")

    def test_sub(self):
        """Tests that the add function is returning an appropriate tuple"""
        v1 = (7,8)
        v2 = (3,4)
        subtracted = (RecVec.__sub__(self,v1,v2))
        self.assertEqual(subtracted, (4,4))
        print("Passed Subtraction")

    def test_eq(self):
        v1 = RecVec(3,4)
        v2 = RecVec(3,4)
        self.assertEqual(v1.x,v2.x)
        self.assertEqual(v1.y,v2.y)
        print("Passed Equal")
        
    def test_str(self):
        """Tests that we are returning a readable string."""
        rv = RecVec(3,4)
        self.assertEqual(str(rv),"RecVec(x = {} y = {})".format(rv.x,rv.y))
        print("String Test Passed!")
        
#     def test_pol(self):

#     def test_rec(self):

#     def test_get_x(self):

    
#     def test_get_y(self):

    def test_get_mag(self):
        """Tests to make sure that the objects magnitude is properly returned"""
        rv = RecVec(3,4)
        magnitude = rv.mag()
        self.assertEqual(magnitude,(rv.x**2 + rv.y**2)*0.5**2)
        print("Get Mag Passed")

#   def test_get_ang(self):


class TestPolVec(unittest.TestCase):
    def test_init(self):
        pv = PolVec(6,10)
        self.assertEqual(pv.mag, 6)
        self.assertEqual(pv.angle, 10)
        print("PolVec Test Passed!")

unittest.main()