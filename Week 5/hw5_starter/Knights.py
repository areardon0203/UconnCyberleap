def memo_knight_moves(k_idx):
    storedMove =[]
    return knight_moves(k_idx,storedMove)

def solveable(p_idxs, k_idx):
    """Returns True (false) if all pawn locations can be capture by sequential knight moves"""
    # 1) Base case - is the puzzle solved?
    for i in p_idxs:
        if i == k_idx: return True 

    # 2) Find all valid_moves

    # 3) Try all valid_moves

    # 4) If nothing worked in step 3, there's no solution with the knight in this position


def knight_moves(k_idx,storedMove):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board""" 
    row = [2, 1, -1, -2, -2, -1, 1, 2]
    col = [1, 2, 2, 1, -1, -2, -2, -1]

    x = k_idx[0]
    y = k_idx[1]
    
    storedMove = (x,y)

    for i in range(8):
        newX = x + row[i]
        newY = y + col[i]
        if valid_moves(newX, newY):
            storedMove = (newX, newY)
            k_idx = (newX, newY)
            knight_moves(k_idx, storedMove)
            return storedMove

            
    return storedMove
        
def valid_moves(x,y):
    """Returns set of all valid moves from k_idx, assuming an 8x8 chess board"""
    return not (x < 0 or y < 0 or x >= 8 or y >= 8)
    








k_idx = (0,0)
memo_knight_moves(k_idx)
# assert(knight_moves((k_idx))) == True
