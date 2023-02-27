# def recr_func(n):
#     if n!= 0:
#         return n * recr_func(n-1)
#     else:
#         return 1
    

# x = recr_func(4)

# print(x)

# def greedy_fc(amt,coins):
#     coins.sort(reverse=True)

#     n=0
#     for c in coins:
#         while c <= amt:
#             amt -= c
#             n += 1

#     return n

# def naive_recr(amt, coins):
#     n_opt = amt #assume we have pennies

#     for c in coins:
#         if c == amt: return 1

#         elif c < amt:
#             n = naive_recr(amt - c, coins) + 1

#             if n < n_opt: # update optimnal solution
#                 n_opt = n 

#     return n_opt

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

if __name__ == '__main__':

    coins = [1, 5,21,25]
    assert memo_recr(63,coins) == 3
    assert memo_recr(50,coins) == 2
    assert memo_recr(27,coins) == 3 

    # # coins = [1,5,10,25]
   
 
    print("All done!")