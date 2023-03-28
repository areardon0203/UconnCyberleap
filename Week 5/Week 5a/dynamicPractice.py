

def memo_recr(amt, coins):
    solved = dict()
    return _memo_recr(amt, coins, solved)

def _memo_recr(amt, coins, solved):
    if amt in solved: return solved[amt]

    solved[amt] = amt

    for c in coins:
        if c == amt:
            solved[amt] = 1
            return 1
        
        elif c < amt:
            n = _memo_recr(amt-c, coins, solved) + 1
            
            if n < solved[amt]: solved[amt] = n
    
    return solved[amt]


# keeping track of solved sub-problems


def dyn_fc(amt, coins):
    solved = {i:i for i in range(1, amt+1)}

    for a in range(1, amt+1):
        for c in coins:
            if c == a:
                solved[a] = 1
                break
            elif c < a:
                n = 1 + solved[a-c]  
                if n < solved[a]: solved[a]= n

    return solved[amt]

if __name__ == '__main__':

    coins = [1, 5,21,25]
    assert dyn_fc(63,coins) == 3
    assert dyn_fc(50,coins) == 2
    assert dyn_fc(27,coins) == 3 

    # # coins = [1,5,10,25]
   
 
    print("All done!")