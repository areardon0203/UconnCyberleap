gameboards = [3,1,2,5,2]

def solve_puzzle(): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""

    # 1) Base case: have you found a valid solution?

    length = len(gameboards)
    for i in gameboards:
        if i == length:
            return True
        elif i > length:
            return False
    # 2) Find all valid next-steps

        elif:
            pass

    # 3) Return True if any valid solution is found

        else:
            pass

        