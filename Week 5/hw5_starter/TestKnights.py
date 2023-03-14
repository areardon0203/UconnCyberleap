from Knights import solveable
import unittest

class TestSolveable(unittest.TestCase):
        def testUnsolveable(self):
                """Test a few unsolveable puzzles"""
                k_idx = (3,3)
                p_idxs = [(1,2),(2,1),(6,7)]
                self.assertFalse(solveable(p_idxs,k_idx))
                print("passed simple test, unsolveable")
                
        def testSolveableSimple(self):
                """Test a simple solveable puzzle"""
                k_idx = (3,3)
                p_idxs = [(1,2)]
                self.assertTrue(solveable(p_idxs,k_idx))
                print("passed simple test, solveable")
        def testSolveableHard(self):
                """Test a few more complex solveable puzzles - try to break your recursive algorithm to help you catch any mistakes"""
                k_idx = (3,3)
                p_idxs = [(1,2),(3,1),(5,2),(7,3)]
                self.assertTrue(solveable(p_idxs,k_idx))
                print("passed harder test 1, solveable")

                k_idx = (3,3)
                p_idxs = [(1,2),(2,1),(3,3),(5,4),(6,7),(4,3)]
                self.assertFalse(solveable(p_idxs,k_idx))
                print("passed harder test 2, unsolveable")

unittest.main()