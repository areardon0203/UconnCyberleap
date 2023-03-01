def memo_recr(amt, coins):
    solved = dict()
    return _memo_recr(amt,coins,solved)

def _memo_recr(amt, coins, solved):
    if amt in solved: return solved[amt]

    solved[amt] = amt

    for c in coins:

        if c == amt:
            solved[amt] = 1
            return 1
        
        elif c < amt:
            n = _memo_recr(amt - c, coins, solved) + 1

            if n < solved[amt]: solved[amt] = n
    
    return solved[amt]


x = memo_recr(63, [1,5,10,25])

print(x)


