import random
import unittest
from swaps import swaps_quad, swaps

class TestSwaps(unittest.TestCase):
    def test_sorted(self):
        self.assertEqual(swaps([1,2,3]), 0)

    def test_reverse_sorted(self):
        self.assertEqual(swaps([3,2,1]), 3)

    def test_random(self):
        self.assertEqual(swaps([2,4,3,1]), 4)

    def test_many_sizes(self):
        """Tests that sorts() works with random lists of size 1-100 elements"""
        for n in range(1, 10):
            L = [random.randint(0, n) for i in range(n)]    # create a list with n items
            P = [L]
            K = [L]
            self.assertEqual(swaps(P), swaps_quad(K))       # note the use of brute force to
                                                            # test our new alg's output

if __name__ == '__main__':
    unittest.main()