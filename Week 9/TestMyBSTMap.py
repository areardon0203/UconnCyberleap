import unittest, random
from MyBSTMap import MyBSTMap

class TestMyBSTMap(unittest.TestCase):
    def test_equal_empty(self):
        """ADD DOCSTRING"""
        bst1 = MyBSTMap()
        bst2 = MyBSTMap()
        self.assertEqual(bst1, bst2)

    # def test_equal_multiplenodes(self):
    #     """ADD DOCSTRING"""
    #     bst1 = MyBSTMap()
    #     bst2 = MyBSTMap()
    #     bst1.put(5)
    #     bst1.put(6)
    #     bst1.put(7)

    #     bst2.put(5)
    #     bst2.put(6)
    #     bst2.put(7)
    #     self.assertEqual(bst1,bst2)

    #     print(bst1)
    #     print(bst2)

    # def test_notequal_multiplenodes_difshapes(self):
    #     """ADD DOCSTRING"""
    #     pass
    # def test_notequal_multiplenodes_difkvs(self):
    #     """ADD DOCSTRING"""
    #     pass
    # def test_frompreorder_small(self):
    #     """ADD DOCSTRING"""
    #     pass
    # def test_frompreorder_large(self):
    #     """ADD DOCSTRING"""
    #     pass
    # def test_frompostorder_small(self):
    #     """ADD DOCSTRING"""
    #     pass
    # def test_frompostorder_large(self):
    #     """ADD DOCSTRING"""
    #     pass

unittest.main()