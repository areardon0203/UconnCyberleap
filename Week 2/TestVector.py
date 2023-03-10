import unittest
import math
from Vector import Vector, RecVec, PolVec

class testVector(unittest.TestCase):
    def test_init(self):
        Vector(5,3,543,6)

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
        v1 = RecVec(3,4)
        v2 = RecVec (7,8)
        self.assertEqual(RecVec.__add__(v1,v2), (10,12))
        print("Passed add")

    def test_sub(self):
        """Tests that the add function is returning an appropriate tuple"""
        v1 = RecVec(7,8)
        v2 = RecVec(3,4)
        self.assertEqual(RecVec.__sub__(v1,v2), (4,4))
        print("Passed Subtraction")

    def test_eq(self):
        """Tests that two tuples are eqivelant"""
        v1 = RecVec(3,4)
        v2 = RecVec(7-4,4)
        self.assertEqual(v1.x,v2.x)
        self.assertEqual(v1.y,v2.y)
        print("Passed Equal")
        
    def test_str(self):
        """Tests that we are returning a readable string."""
        rv = RecVec(3,4)
        self.assertEqual(str(rv), f"RecVec(x = 3 y = 4)")
        print("Passed String Test")
        
    def test_pol(self):
        """"Tests that we return the correct polar coordinates from rectangular coordinate input"""
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

    def test_get_ang(self):
        """Tests that the angle returned is correct"""
        rv = RecVec(3,4)
        self.assertEqual(rv.ang(),53)
        print("Passes get_ang")

class TestPolVec(unittest.TestCase):
    """Test the class RecVec in the file Vector.py"""  
    def test_init(self):
        """Tests that a Polar Vector object has been created."""
        pv = PolVec(4,30)
        self.assertEqual(pv.x, 4)
        self.assertEqual(pv.y, 30)
        print("PolVec INIT Test Passed!")

    def test_add(self):
        """Tests that the add function is returning an appropriate tuple"""
        pv1 = PolVec(3,4)
        pv2 = PolVec(7,8)
        self.assertEqual(PolVec.__add__(pv1,pv2), (10,12))
        print("PolVec Passed add")

    def test_sub(self):
        """Tests that the add function is returning an appropriate tuple"""
        pv1 = PolVec(7,8)
        pv2 = PolVec(3,4)
        self.assertEqual(PolVec.__sub__(pv1,pv2), (4,4))
        print("PolVec Passed Subtraction")

    def test_eq(self):
        """Tests that two tuples are eqivelant"""
        pv1 = PolVec(3,4)
        pv2 = PolVec(7-4,4)
        self.assertEqual(pv1.x,pv2.x)
        self.assertEqual(pv1.y,pv2.y)
        print("Passed Equal")
        
    def test_str(self):
        """Tests that we are returning a readable string."""
        pv = PolVec(3,4)
        self.assertEqual(str(pv), f"PolVec(x = 3 y = 4)")
        print("Passed String Test Pol")
        
    def test_pol(self):
        """"Tests that we return the correct polar coordinates from rectangular coordinate input"""
        pv = PolVec(3,4)
        PolToRec = pv.pol()
        self.assertEqual(PolToRec,(5, 53))
        print("Passed Polar Coordinate test Pol")

    def test_rec(self):
        """Tests to make sure that the rectangular coordinates are returned in a tuple"""
        pv = PolVec(5,53)
        polConvert = PolVec.rectangular(pv)
        self.assertEqual(polConvert,(3,4))
        print("Passed Polar to Rec test")

    def test_get_x(self):
        """Tests that the value of x is returned properly as a single value"""
        rv = PolVec(3,4)
        self.assertEqual(rv.get_x(),3)
        print("Passed PolVec get_x")
    
    def test_get_y(self):
        """Tests that the value of y is returned properly as a single value"""
        rv = PolVec(3,4)
        self.assertEqual(rv.get_y(),4)
        print("Polvec Passed get_y")

    def test_get_mag(self):
        """Tests to make sure that the objects magnitude is properly returned"""
        rv = PolVec(3,40)
        self.assertEqual(rv.mag(),(3))
        print("Passed get_mag")

    def test_get_ang(self):
        """Tests that the angle returned is correct"""
        rv = PolVec(5,40)
        self.assertEqual(rv.ang(),40)
        print("Passes get_ang")             

unittest.main()