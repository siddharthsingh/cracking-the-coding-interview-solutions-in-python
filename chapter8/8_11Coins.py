def count(n, coins, max_taken):
    if n==0:return 1
    # print(max_taken)
    global store
    if (n,max_taken) in store:
        return store[(n,max_taken)]
    ans = 0
    for coin in coins:
        if coin <= n and coin <= max_taken:
            # ans += n//coin
            ans += count(n - coin, coins, coin)
    store[(n,max_taken)] = ans
    return ans
store = {}
coins = [5,2,1]

print(count(136,coins,5))