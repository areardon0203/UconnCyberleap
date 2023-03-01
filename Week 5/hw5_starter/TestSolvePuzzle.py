from SolvePuzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                
                x = solve_puzzle([2, 1, 4])
                assert x == True

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                
                y = solve_puzzle([3, 1, 4])
                assert y == False
        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""

                z = solve_puzzle([2,2,1,4])
                assert z == True

        def testUnsolveable(self):
                """Tests an unsolveable board"""

                l = solve_puzzle([1,2,2])
                assert l == True
unittest.main()







