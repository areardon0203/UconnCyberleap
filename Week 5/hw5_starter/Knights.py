def solveable(p_idxs, k_idx):
    """Returns True (false) if all pawn locations can be capture by sequential knight moves"""
    # 1) Base case - is the puzzle solved?
    if len(p_idxs) == 0: return True

    # 2) Find all valid_moves
    valid_moves_list = valid_moves(k_idx)

    # 3) Try all valid_moves
    for pawn in p_idxs:
        if pawn in valid_moves_list:
            p_idxs.remove(pawn)
            k_idx_new = pawn
            if solveable(p_idxs,k_idx_new):
                return True
    return False
            
    # 4) If nothing worked in step 3, there's no solution with the knight in this position


def valid_moves(k_idx):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board""" 
    valid_set = set()

    idx_mod = {(2,1),(2,-1),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)}
    for row, col in idx_mod:
        if board_check(k_idx[0]+row,k_idx[1]+col):
            valid_set.add((k_idx[0]+row,k_idx[1]+col))
    
    return valid_set
        
def board_check(x,y):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board"""
    return not (x < 0 or y < 0 or x > 7 or y > 7)
