def minimum_coins(coins, amount):
    mini = [amount + 1] * (amount + 1)
    mini[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                mini[i] = min(mini[i], mini[i - coin] + 1)
                
    return mini[amount] if mini[amount] != amount + 1 else -1
coins = [1, 2, 5]
amount = 11

print(minimum_coins(coins, amount))
