from SolvePuzzle import memo_solve_puzzle as puzzle

import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                
                x = puzzle([2, 1, 4])
                assert x == True

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                
                y = puzzle([3, 1, 4])
                assert y == False

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""

                z = puzzle([2,2,1,4])
                assert z == True

        def testUnsolveable(self):
                """Tests an unsolveable board"""

                l = puzzle([1,2,2])
                assert l == True

        print("all good!")
unittest.main()







