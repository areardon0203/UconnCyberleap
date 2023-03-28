from SolvePuzzle import memo_solve_puzzle as puzzle

import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                x = [2, 1, 4]
                self.assertTrue(puzzle(x))
                print("clockwise works")

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                y = [1, 2, 4]
                self.assertTrue(puzzle(y))
                print('counter clockwise works')

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                z = [2,2,3,4]
                self.assertTrue(puzzle(z))
                print("combo moves works")


        def testUnsolveable(self):
                """Tests an unsolveable board"""
                q = [2,3,2,4]
                self.assertFalse(puzzle(q))
                print("this puzzle is unsolveable")
        print("all good!")

unittest.main()







