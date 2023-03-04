def memo_solve_puzzle(board, idx=0):
    solved ={}
    return _solve_puzzle(board, idx, solved)


def _solve_puzzle(board, idx, solved):
    if idx in solved: return solved[idx]
    if idx == len(board) - 1: return True

    solved[idx] = idx

    idx_cw = (idx + board[idx]) % len(board)

    idx_ccw = (idx - board[idx]) % len(board)

    n = False

    for move in {idx_cw, idx_ccw}:
        
        # if current_optimum == True:
        #     return solved[idx] == True
        if move not in solved:
            n = _solve_puzzle(board, move, solved)
        
            if n is not False:   
                solved[idx] = n
                return solved[idx]
            
    return solved[idx]

