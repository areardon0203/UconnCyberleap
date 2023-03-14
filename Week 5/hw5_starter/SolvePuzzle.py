def memo_solve_puzzle(board, idx=0, solved=None):
    """This function stores a cache of solved results"""
    if solved is None:
        solved ={}
    return _solve_puzzle(board, idx, solved)


def _solve_puzzle(board, idx, solved):
    """This function checks if the puzzle is solveable or not"""
    #base case
    if idx in solved: return solved[idx] 
    if idx == len(board) - 1: return True

    solved[idx] = False

    #stores values of clockwise and counter clock movement from current space
    idx_cw = (idx + board[idx]) % len(board)
    idx_ccw = (idx - board[idx]) % len(board)
    
    # n = False

    
    for move in {idx_cw, idx_ccw}:
        if move not in solved and _solve_puzzle(board,move,solved):
            solved[idx] = True
            return True
               
    return solved[idx]
    

        # if current_optimum == True:
        #     return solved[idx] == True




    if idx_cw not in solved:
        if _solve_puzzle(board, idx_cw, solved):
            solved[idx] = True
            return True
            
    if idx_ccw not in solved:
        if _solve_puzzle(board, idx_ccw, solved):
            solved[idx] = True
            return True