# def memo_recr(amt,coins):                               #Defeine our helper class
#     solved = dict()                                     # create an empty dictionary
#     return _memo_recr(amt,coins,solved)                 # run our main function with newly created dictionary solved


# def _memo_recr(amt, coins, solved):
#     if amt in solved :return solved[amt]                # if already a solution return solution


#     solved[amt] = amt                                    #initializes the dictionary solved to be full number

#     print(solved[amt])
#     for c in coins:                                     # represents each coin in the list of coins
#         if c == amt:                                    # if the current coins is the amount, immediately return 1(base case)
#             solved[amt] = 1
#             return 1
            
#         elif c < amt:                                   # if coin is less than the total amount
#             n = _memo_recr(amt - c,coins,solved) + 1    # give a cost of 1 and run equation with newly subtracted amount 

#             if n < solved[amt]: solved[amt]= n          # if the current path is less than stored optimum, the current path becomes the stored optimum
#     return solved[amt]                                  # return the current stored optimum


# print(memo_recr(10,[1,5,10,25]))                        # Run our fucntion and print the return results




def memo_recr(amt,coins):
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
            n = _memo_recr(amt - c,coins,solved) + 1

            if n < solved[amt]: solved[amt] = n

    return solved[amt]


print(memo_recr(63,[1,5,10,25]))