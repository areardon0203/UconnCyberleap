import unittest, random
from MyBSTMapiter import MyBSTMap

class TestMyBSTMap(unittest.TestCase):
    def test_equal_empty(self):
        """ADD DOCSTRING"""
        bst1 = MyBSTMap()
        bst2 = MyBSTMap()
        print('empty')
        self.assertEqual(bst1, bst2)

    def test_equal_multiplenodes(self):
        """ADD DOCSTRING"""
        bst1 = MyBSTMap()
        bst2 = MyBSTMap()
        bst1.put(5)
        bst1.put(6)
        bst1.put(7)

        bst2.put(5)
        bst2.put(6)
        bst2.put(7)
        self.assertEqual(bst1,bst2)
        print("equal")
        print(bst1)
        print(bst2)

    def test_notequal_multiplenodes_difshapes(self):
        """ADD DOCSTRING"""
        bst1 = MyBSTMap()
        bst2 = MyBSTMap()
        bst1.put(5)
        bst1.put(6)
        bst1.put(7)

        bst2.put(4)
        bst2.put(2)
        bst2.put(1)
        bst2.put(5)
        self.assertNotEqual(bst1,bst2)
        print('not equal')
        print(bst1)
        print(bst2)

    def test_notequal_multiplenodes_difkvs(self):
        """ADD DOCSTRING"""
        bst1 = MyBSTMap()
        bst2 = MyBSTMap()
        bst1.put(2)
        bst1.put(3)
        bst1.put(1)

        bst2.put(24)
        bst2.put(2)
        bst2.put(6)
        print("not Equal")
        self.assertNotEqual(bst1,bst2)
        print(bst1)
        print('-' * 20)
        print(bst2)

    def test_frompreorder_small(self):
        """ADD DOCSTRING"""
        
        bst1 = MyBSTMap()
        for k in [3, 1, 2]:                           #  Build the tree shown above
            bst1.put(k, str(k))
        print("This is bst1: ")
        print(bst1)
        # L = [(k, v) for (k, v) in bst1.preorder()]  # construct preorder list
        # bst2 = MyBSTMap.frompreorder(L)             # reconstruct the original bst
        # bst1 == bst2                                # verify trees are equal



    def test_frompreorder_large(self):
        """ADD DOCSTRING"""
        pass
    def test_frompostorder_small(self):
        """ADD DOCSTRING"""
        pass
    def test_frompostorder_large(self):
        """ADD DOCSTRING"""
        pass

unittest.main()