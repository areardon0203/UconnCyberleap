def fewest_coins(amt, coins):

    if amt in coins: return 1

    valid_coins=[coin for coin in coins if coin <=amt]

    current_optimum = amt

    for coin in valid_coins:
        path_optimum = 1 + fewest_coins(amt - coin, coins)
        if path_optimum < current_optimum:
            current_optimum = path_optimum

    return current_optimum

coins = [1,10,25]

x = fewest_coins(63,coins)

print(x)