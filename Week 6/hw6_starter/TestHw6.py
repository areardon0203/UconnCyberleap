import unittest, random
from hw6 import cocktail_sort, opt_insertion_sort, bs_sublist

#TODO: implement unittests below. Use docstrings, whitespace, and comments.
# Hint 1 - start by defining a function that checks if a list is sorted
# Hint 2 - fix the random seed (`random.seed(NUMBER)`) to make your bugs consistent (makes debugging easier)
# Hint 3 - use assertCountEqual(L1, L2) to ensure your final sorted list has the same items
#          as your initial list

class TestCocktailSort(unittest.TestCase):
   def test_Sorted(self):
      # Test case for a sorted list
      input_list = [1, 2, 3, 4, 5]
      expected_output = [1, 2, 3, 4, 5]
      cocktail_sort(input_list)
      self.assertEqual(input_list, expected_output)
      print("sorted done!")
        
   def test_Reverse(self):
      # Test case for a reverse-sorted list
      input_list = [5, 4, 3, 2, 1]
      expected_output = [1, 2, 3, 4, 5]
      cocktail_sort(input_list)
      self.assertEqual(input_list, expected_output)
      print("reverse done!")

   def test_Random(self):
      # Test case for a list with random elements
      input_list = [5, 2, 8, 4, 7, 1, 3, 6]
      expected_output = [1, 2, 3, 4, 5, 6, 7, 8]
      cocktail_sort(input_list)
      self.assertEqual(input_list, expected_output)
      print("random done!")
  
   def test_ArbitrarySize(self):
      # Test case for a list with arbitrary size
      input_list = [1, 4, 2, 6, 3, 5, 8, 7, 9]
      expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      cocktail_sort(input_list)
      self.assertEqual(input_list, expected_output)
      print("arbitrary done!")

# class TestOptInsertionSort(unittest.TestCase):
#    def test_Sorted(self):
#       # Test case for a sorted list
#       input_list = [1, 2, 3, 4, 5]
#       expected_output = [1, 2, 3, 4, 5]
#       opt_insertion_sort(input_list)
#       self.assertEqual(input_list, expected_output)
        
#    def test_Reverse(self):
#       # Test case for a reverse-sorted list
#       input_list = [5, 4, 3, 2, 1]
#       expected_output = [1, 2, 3, 4, 5]
#       opt_insertion_sort(input_list)
#       self.assertEqual(input_list, expected_output)
        
#    def test_Random(self):
#       # Test case for a list with random elements
#       input_list = [5, 2, 8, 4, 7, 1, 3, 6]
#       expected_output = [1, 2, 3, 4, 5, 6, 7, 8]
#       opt_insertion_sort(input_list)
#       self.assertEqual(input_list, expected_output)
        
#    def test_ArbitrarySize(self):
#       # Test case for a list with arbitrary size
#       input_list = [1, 4, 2, 6, 3, 5, 8, 7, 9]
#       expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#       opt_insertion_sort(input_list)
#       self.assertEqual(input_list, expected_output)

# bs_sublist tests are provided for you.
class TestBinarySearchSublist(unittest.TestCase):
   def testExtremes(self):
      """Tests binary search on items less than min or greater than max of sublist"""
      #id:  0    1    2    3    4    5    6    7
      L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
      #         |--------sorted sublist---------|
      self.assertEqual(bs_sublist(L, left=1, right=7, item='a'), 0)

      # item = 'a'
      # left      right    med
      # 1         7        4
      # 1         4        2
      # 1         2        1
      # 1         1        1  Base Case
      #                       L[1] < 'a' - 'a' goes at pos 1
      #                       L[1] == 'a' = 'a' goes at pos 0
      #                       L[1] > 'a' = 'a' goes at pos 0

      #id:  0    1    2    3    4    5    6    7
      L = ['i', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
      #         |--------sorted sublist---------|
      self.assertEqual(bs_sublist(L, left=1, right=7, item='i'), 7)

      n = 1000
      L = [i for i in range(n)] # sorted list of n items

   def testWithinUnique(self):
      """Tests binary search on items within the bounds of a sublist, but does not appear in that sublist"""
      #id:  0    1    2    3    4    5    6    7
      L = ['?', 'a', 'c', 'e', 'g', 'i', 'k', 'm']
      #         |--------sorted sublist---------|
      for i, char in enumerate('bdfhjl'):
         L[0] = char
         self.assertEqual(bs_sublist(L, left=1, right=7, item=char), 1+i)
      #  self.assertEqual(bs_sublist(L, left=1, right=7, item='b'), 1)

      # item = 'b'
      # left      right    med
      # 1         7        4
      # 1         4        2
      # 1         2        1
      # 2         2        2  Base Case
      #                       item < L[2]  - return 1
      #                       item == L[2] - return 1
      #                       item > L[2]  - return 2


   def testWithinDuplicate(self):
      """Tests binary search on item within the bounds of a sublist, that do appear in that sublist. Should return the minimum index."""
      #id:  0    1    2    3    4    5    6    7
      L = ['?', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
      #         |--------sorted sublist---------|

      for i, char in enumerate('abcdefgh'):
         self.assertEqual(bs_sublist(L, left=1, right=7, item=char), i)

   def testArbitrarySize(self):
      """Tests binary search on sublists of arbitrary size"""
      lower = 'abcdefghijklmnopqrstuvwxyz'

      for n in range(2, 27):
         L = [lower[i] for i in range(n)]
         self.assertEqual(bs_sublist(L, left=1, right=n-1, item='a'), 0)      # ['a', 'b', ...] returns 0

         for i, char in enumerate(lower[1:n]):
            L[0] = char
            self.assertEqual(bs_sublist(L, left=1, right=n-1, item=char), i)  # ['?', b', ...] returns i

      # n = 2
      # id:  0    1    2    3    4    5    6    7
      # L = ['a', 'b',]   # pos = 0
      # L = ['b', 'b',]   # pos = 0
      # L = ['c', 'b',]   # pos = 1
      #           |--------sorted sublist---------|
      # n = 3
      # L = ['a', 'b', 'c']  # pos = 0
      # L = ['b', 'b', 'c']  # pos = 0
      # L = ['c', 'b', 'c']  # pos = 1
      # L = ['d', 'b', 'c']  # pos = 2

      # n = 4
      # L = ['a', 'b', 'c', 'd']   # pos = 0
      # L = ['b', 'b', 'c', 'd']   # pos = 0
      # L = ['c', 'b', 'c', 'd']   # pos = 1
      # L = ['d', 'b', 'c', 'd']   # pos = 2
      # L = ['e', 'b', 'c', 'd']   # pos = 3

      # n = 5
      # L = ['a', 'b', 'c', 'd', 'e']   # pos = 0
      # L = ['b', 'b', 'c', 'd', 'e']   # pos = 0
      # L = ['c', 'b', 'c', 'd', 'e']   # pos = 1
      # L = ['d', 'b', 'c', 'd', 'e']   # pos = 2
      # L = ['e', 'b', 'c', 'd', 'e']   # pos = 3
      # L = ['f', 'b', 'c', 'd', 'e']   # pos = 4

unittest.main()