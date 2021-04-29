def solve(coins, n):
    nc = n
    s = []

    while coins:
        coin = coins.pop(0)
        while (nc - coin) >= 0:
            s.append(coin)
            nc -= coin
        if nc == 0:
            break
    
    print(f"Coins: {s}")

if __name__ == '__main__':
    coins = [1, 3, 4]
    n = 6
    coins = coins[::-1]
    solve(coins, n)