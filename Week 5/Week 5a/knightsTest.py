def solveable(p_idxs, k_idx):
    """Returns True (false) if all pawn locations can be capture by sequential knight moves"""
    # 1) Base case - is the puzzle solved?
    if len(p_idxs) == 0:
        return True

    # 2) Find all valid_moves
    valid_moves = knight_moves(k_idx)

    # 3) Try all valid_moves


    for row, col in valid_moves:
        if is_valid_move(k_idx[0] + row, k_idx[1] + col):
            new_knight = (k_idx[0] + row, k_idx[1] + col)
            new_pawns = p_idxs - {new_knight}
            if solveable(new_pawns, new_knight):
                return True
        
    # 4) If nothing worked in step 3, there's no solution with the knight in this position
    return False


def knight_moves(k_idx):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board"""
    idx_mod = {(2, 1), (2, -1), (-2, 1), (-2, -1), (-1, -2), (1, -2), (-1, 2), (1, 2)}
    valid_moves = set()
    for row, col in idx_mod:
        if is_valid_move(k_idx[0] + row, k_idx[1] + col):
            valid_moves.add((row, col))
    return valid_moves


def is_valid_move(x, y):
    """Returns True if the move is valid on an 8x8 chess board"""
    return 0 <= x < 8 and 0 <= y < 8


# Example usage:
pawns = {(2, 2), (3, 4), (1, 5)}
knight = (0, 0)
print(solveable(pawns, knight))  # Expected output: True
