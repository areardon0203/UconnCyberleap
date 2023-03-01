
def solve_puzzle(gameboard): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""



    # 1) Base case: have you found a valid solution?

    length = len(gameboard) - 1

    for i in gameboard:
        if i == length: return True

    # 2) Find all valid next-steps:

        # elif:
        #     pass

    # 3) Return True if any valid solution is found

        else:
            return True

if __name__ == '__main__':

    x = solve_puzzle([2, 1, 4])
    assert x == True

    y = solve_puzzle([3, 1, 4])
    assert y == False

    z = solve_puzzle([2,2,1,4])
    assert z == True

    l = solve_puzzle([1,2,2])
    assert l == True