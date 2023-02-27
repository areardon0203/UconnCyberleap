gameboard = [2,3,2,5,4]
gameboard2 = [8,2,7,3,5]

# def memo_solve():
#     Solved = dict()
#     return _memo_recr(amt, coins, solved)
    

def solve_puzzles(board):
    bl = len(board)
    for space in board:
        if space == board [-1]:
            return True


solve_puzzles(gameboard)
# if __name__ == '__main__':
#     assert solve_puzzles(gameboard) == True
#     print("base case works!")

#     assert solve_puzzles(gameboard2) == False
#     print("unsolved case works!")
