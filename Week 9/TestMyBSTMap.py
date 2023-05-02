import unittest, random
from MyBSTMap import MyBSTMap

class TestMyBSTMap(unittest.TestCase):
    def test_equal_empty(self):
        """ADD DOCSTRING"""
        bst1 = MyBSTMap()
        bst2 = MyBSTMap()
        print('empty')
        self.assertEqual(bst1, bst2)

    def test_equal_multiplenodes(self):
        """5
            \
             6
              \
               7"""

        
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
        """5
            \
             6
              \
               7"""

        bst1.put(5)
        bst1.put(6)
        bst1.put(7)


        """4
          / \
         2   5
        /     
       1       """
        bst2.put(4)
        bst2.put(2)
        bst2.put(1)
        bst2.put(5)
        self.assertNotEqual(bst1,bst2)
        print('not equal')
        print(bst1)
        print(bst2)

    def test_notequal_multiplenodes_difkvs(self):
        """2
          / \ 
         1   3
        """
        bst1 = MyBSTMap()
        bst2 = MyBSTMap()
        bst1.put(2)
        bst1.put(3)
        bst1.put(1)
        """24
          / \ 
         2   6
        """
        bst2.put(24)
        bst2.put(2)
        bst2.put(6)
        print("not Equal")
        self.assertNotEqual(bst1,bst2)
        print(bst1)
        print('-' * 20)
        print(bst2)

    def test_frompreorder_small(self):
        """Tests if the frompreorder function is returning a preordered tree that is added in the same order using small dataset"""
        
        bst1 = MyBSTMap()
        for k in [5, 7, 3, 2, 1]:                               #  Build the tree shown above
            bst1.put(k, str(k))
        L = [(k, v) for (k, v) in bst1.preorder()]              # construct preorder list
        bst2 = MyBSTMap.frompreorder(L)                         # reconstruct the original bst
        self.assertEqual(bst1,bst2)                             # verify trees are equal
        print("Passed short from pre order test!")
        
    def test_frompreorder_large(self):
        """Tests if the frompreorder function is returning a preordered tree that is added in the same order using large dataset"""
        bst1 = MyBSTMap()
        randomlist = random.sample(range(1, 1000), 999)
        for k in [randomlist]:                                #  Build the tree shown above
            bst1.put(k, str(k))
        L = [(k, v) for (k, v) in bst1.preorder()]         # construct preorder list
        bst2 = MyBSTMap.frompreorder(L)                    # reconstruct the original bst
        self.assertEqual(bst1,bst2)                                # verify trees are equal
        print("Passed long from pre order test!")


    def test_frompostorder_small(self):
        """Tests if the frompostorder function is returning a postordered tree that is added in the same order using small dataset"""

        bst1 = MyBSTMap()
        for k in [5, 7, 3, 2, 1]:                                #  Build the tree shown above
            bst1.put(k, str(k))
        L = [(k, v) for (k, v) in bst1.postorder()]         # construct preorder list
        bst2 = MyBSTMap.frompostorder(L)                    # reconstruct the original bst
        self.assertEqual(bst1,bst2)                                # verify trees are equal
        print("Passed short from post order test!")
        
    def test_frompostorder_large(self):
        """Tests if the frompostorder function is returning a postordered tree that is added in the same order using large dataset"""
        bst1 = MyBSTMap()
        randomlist = random.sample(range(1, 1000), 999)
        for k in [randomlist]:                                #  Build the tree shown above
            bst1.put(k, str(k))
        L = [(k, v) for (k, v) in bst1.postorder()]         # construct preorder list
        bst2 = MyBSTMap.frompostorder(L)                    # reconstruct the original bst
        self.assertEqual(bst1,bst2)                                # verify trees are equal
        print("Passed long from post order test!")

unittest.main()