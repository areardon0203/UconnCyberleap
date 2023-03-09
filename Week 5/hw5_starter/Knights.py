def solveable(p_idxs, k_idx):
    """Returns True (false) if all pawn locations can be capture by sequential knight moves"""
    # 1) Base case - is the puzzle solved?
    if len(p_idx) == 0: return True

    # 2) Find all valid_moves
    valid_moves = knight_moves(k_idx)

    # 3) Try all valid_moves

    for row, col in idx_mod:
        if valid_moves(k_idx[0]+row,k_idx[1]+col):
            valid_set.add(row,col)


    return False

    # 4) If nothing worked in step 3, there's no solution with the knight in this position


def knight_moves(k_idx):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board""" 

    idx_mod = {(2,1),(2,-1),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)}
    return idx_mod



        
def valid_moves(x,y):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board"""
    return not (x < 0 or y < 0 or x >= 8 or y >= 8)
    








k_idx = (0,0)
knight_moves(k_idx)

